from setting.db import db
from datetime import datetime
from sqlalchemy import (
    JSON,
    REAL,
    TEXT,
    TIMESTAMP,
    Boolean,
    Column,
    Enum,
    Integer,
    String,
    ForeignKey,
    Float,
)
class ScreenshotModel(db.Model):
    __tablename__ = "screen_shots"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, unique=True, nullable=False)

    latitude = Column(Float(precision=5), unique=False, nullable=False)
    longitude = Column(Float(precision=5), unique=False, nullable=False)
    begin_at = Column(TIMESTAMP, nullable=False)
    end_at = Column(TIMESTAMP, nullable=False)

    media_type = Column(String, unique=True, nullable=False)
    credential = Column(String)
    storage_address = Column(String)

    media_source_id = Column(Integer, ForeignKey("media_sources.id"), nullable=True)
    map_id = Column(Integer, ForeignKey("maps.id"), nullable=True)
    layer_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    sensor_id = Column(Integer, ForeignKey("sensors.id"), nullable=True)
    unity_id = Column(Integer, ForeignKey("unities.id"), nullable=True)
    official_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(String, unique=True, nullable=False)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(Integer,nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)
