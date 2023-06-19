from setting.db import db
from datetime import datetime

from sqlalchemy import (
    TEXT,
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
)


class MarkerModel(db.Model):
    __tablename__ = "markers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)

    type = Column(String, unique=False, nullable=False)
    color = Column(String, unique=False, nullable=False)

    sensor_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    facility_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    symbol_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=True)
    layer_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=True)
    description = Column(TEXT)
    latitude = Column(Float(precision=5), unique=False, nullable=False)
    longitude = Column(Float(precision=5), unique=False, nullable=False)

    hierarchy_id = Column(
        Integer, ForeignKey("hierarchies.id"), unique=False, nullable=False
    )

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
