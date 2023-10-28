import uuid
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.sql.expression import cast, extract
from sqlalchemy.types import String
from sqlalchemy.orm import Query
from sqlalchemy.orm import class_mapper

from typing import List, Any, Dict
from datetime import date, datetime

from .types import sqlalchemy_to_python_types
from .constants import MONTHS
from .validators import is_uuid


class Paginator:
    def __init__(
        self, session: Session, model: DeclarativeMeta, close_session: bool = False
    ) -> None:
        """
        Initializes a new instance of the class.

        Args:
            session (Session): The session to use for the database connection.
            model (DeclarativeMeta): The model to use for database operations.
            close_session (bool, optional): Indicates whether to close the session after use. Defaults to False.
        """
        self.session = session
        self.model = model
        self.close_session = close_session

    def apply_filters(self, query: Session, filters_dict: Dict[str, Any]) -> Session:
        """
        Apply filters to the query based on the given filter dictionary.

        Args:
            query: The SQLAlchemy session query object.
            filters_dict: A dictionary containing the filters to be applied.

        Returns:
            The modified SQLAlchemy session query object.

        Raises:
            Exception: If there is an error during filtering.

        """
        try:
            for column, value in filters_dict.items():
                if hasattr(self.model, column):
                    column_attr = getattr(self.model, column)

                    if column_attr.type.python_type == uuid.UUID:
                        query = query.filter(column_attr == str(value))

                    elif column_attr.type.python_type == str and is_uuid(value):
                        query = query.filter(column_attr == str(value))

                    elif column_attr.type.python_type == str:
                        ililike_column = cast(column_attr, String).ilike(
                            f"%{value}%", escape="\\"
                        )
                        query = query.filter(ililike_column)

                    elif column_attr.type.python_type in (date, datetime):
                        if value.lower() in MONTHS:
                            month_number = datetime.strptime(value, "%B").month
                            query = query.filter(
                                extract("month", column_attr) == month_number
                            )
                        elif value.isdigit() and len(value) == 4:
                            year_number = int(value)
                            query = query.filter(
                                extract("year", column_attr) == year_number
                            )
                        elif "-" in value:
                            try:
                                date_value = datetime.strptime(value, "%Y-%m-%d")
                                query = query.filter(
                                    func.date(column_attr) == date_value.date()
                                )
                            except ValueError:
                                query = query.filter()
                        else:
                            query = query.filter()

                    else:
                        query = query.filter(column_attr == value)

            self.session.commit()
            return query
        except Exception as error:
            self.session.rollback()
            raise error
        finally:
            if self.close_session:
                self.session.close()

    def get_items(
        self,
        filters: Dict[str, Any],
        page_number: int = 1,
        page_size: int = 100,
        serialize: bool = False,
    ) -> List[Any]:
        """
        Retrieve a list of items from the database.

        Args:
            filters (Dict[str, Any]): A dictionary of filters to apply to the query.
            page_number (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 100.
            serialize (bool, optional): Whether to serialize the objects to JSON. Defaults to False.

        Returns:
            List[Any]: A list of items that match the filters.
        """
        offset = (page_number - 1) * page_size
        query: Query = self.session.query(self.model)
        query = self.apply_filters(query, filters)
        query = query.offset(offset).limit(page_size)

        if serialize:
            json_objects = [self.__sqlalchemy_to_dict(obj) for obj in query]
            return json_objects
        return query.all()

    def __sqlalchemy_to_dict(
        self, obj: Any, exclude_keys: List[str] = []
    ) -> Dict[str, Any]:
        """
        Convert an SQLAlchemy object to a dictionary.

        Args:
            obj (Any): The SQLAlchemy object to convert.
            exclude_keys (List[str], optional): The list of keys to exclude from the conversion. Defaults to [].

        Returns:
            Dict[str, Any]: The dictionary representation of the SQLAlchemy object.
        """
        mapper = class_mapper(obj.__class__)
        columns = [column.key for column in mapper.columns]

        data: Dict[str, Any] = {}
        for column in columns:
            if column in exclude_keys:
                continue

            try:
                column_value = getattr(obj, column)
                if isinstance(column_value, (str, int, float, bool, dict, list)):
                    data[column] = column_value
                else:
                    data[column] = (
                        sqlalchemy_to_python_types.get(type(column_value))(column_value)
                        if column_value
                        else None
                    )
            except Exception:
                continue

        return data
