from setting.db import db
from datetime import datetime

from sqlalchemy import (
    TEXT,
    Column,
    Integer,
    ForeignKey,
    TIMESTAMP
)


class MapNoteModel(db.Model):
    __tablename__ = "markers"

    id = Column(Integer, primary_key=True)
    note = Column(TEXT)
    sensor_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    facility_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    symbol_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=True)
    layer_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=True)

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
