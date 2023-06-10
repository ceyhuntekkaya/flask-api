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
)
class SensorImageModel(db.Model):
    __tablename__ = "sensor_images"

    # Information
    id = Column(Integer, primary_key=True)
    image = Column(TEXT)
    image_order = Column(Integer)

    # Timing
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    # Relation
    sensor_id = Column(Integer, db.ForeignKey("sensors.id"))