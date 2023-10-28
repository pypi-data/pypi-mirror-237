from sqlalchemy import (
    String,
    Integer,
    SmallInteger,
    BigInteger,
    Float,
    Numeric,
    Date,
    DateTime,
    Boolean,
    Enum,
    Interval,
    JSON,
    LargeBinary,
    Text,
    MetaData,
)
from sqlalchemy.dialects.postgresql import UUID
from datetime import date, datetime, timedelta
from decimal import Decimal
from uuid import UUID as UUID_PYTHON_TYPE


python_types = {
    datetime: str,
    UUID_PYTHON_TYPE: str,
    date: str,
    str: str,
    int: int,
    float: float,
    bool: bool,
    dict: dict,
    bytes: bytes,
    list: list,
    Decimal: float,
}


sqlalchemy_to_python_types = {
    String: str,
    Integer: int,
    SmallInteger: int,
    BigInteger: int,
    Float: float,
    Numeric: Decimal,
    Date: date,
    DateTime: datetime,
    Boolean: bool,
    Enum: str,
    Interval: timedelta,
    JSON: dict,
    LargeBinary: bytes,
    Text: str,
    UUID: str,
    MetaData: dict,
    **python_types,
}
