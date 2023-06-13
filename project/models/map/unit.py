from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TEXT,
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
)


class UnitModel(db.Model):
    __tablename__ = "unities"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    description = Column(TEXT)

    unit_type = Column(String)  # dost düşman
    unit_parent = Column(String)  # motorize kara deniz
    unit_sub = Column(String)  # piyade
    symbol_code = Column(String)  # app code
    critical_unit_type = Column(String, unique=False, nullable=True)

    layer_id = Column(
        Integer, ForeignKey("layers.id"), unique=False, nullable=False
    )
    hierarchy_id = Column(
        Integer, ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    official_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
