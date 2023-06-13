from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TEXT,
    Column,
    Integer,
    String,
)


class SymbolModel(db.Model):
    __tablename__ = "symbols"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    source = Column(String, unique=False, nullable=False)
    main_type = Column(String)  # birlik mi - silah mı- tesis mi
    description = Column(TEXT)
    status = Column(Integer, default=1)
