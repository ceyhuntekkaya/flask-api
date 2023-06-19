from setting.db import db
from datetime import datetime
from sqlalchemy import (
    JSON,
    REAL,
    TEXT,
    TIMESTAMP,
    Boolean,
    Column,
    Integer,
    String,
    ForeignKey,
    ARRAY,
    Float
)


class EquipmentModel(db.Model):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True)
    source = Column(String, unique=False, nullable=False)
    description = Column(TEXT)
    unit_id = Column(Integer, ForeignKey("units.id"), unique=False, nullable=False)
    name = Column(String, unique=True, nullable=False)
    equipment_type = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )