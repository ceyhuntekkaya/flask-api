from sqlalchemy.orm import relationship, MappedColumn

from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TEXT,
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
    Float
)


class UnitModel(db.Model):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(TEXT)
    base_unit_id = MappedColumn(
        Integer, ForeignKey("units.id"), nullable=True
    )

    unit_type = Column(String)  # dost düşman
    unit_command = Column(String)
    hierarchy_id = Column(
        Integer, ForeignKey("hierarchies.id"), nullable=False
    )
    unit_parent = Column(String)  # motorize kara deniz
    unit_sub = Column(String)  # piyade
    symbol_code = Column(String)  # app code
    critical_unit_type = Column(String)
    latitude = Column(Float(precision=5), nullable=False)
    longitude = Column(Float(precision=5), nullable=False)
    status = Column(Integer, default=1)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
