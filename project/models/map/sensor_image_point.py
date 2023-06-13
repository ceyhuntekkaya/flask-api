from setting.db import db
from datetime import datetime
from sqlalchemy import (
    JSON,
    TIMESTAMP,
    Column,
    Integer,
    ForeignKey,
)


class SensorImagePointModel(db.Model):
    __tablename__ = "sensor_image_points"

    # Information
    id = Column(Integer, primary_key=True)

    points = Column(JSON)

    # Timing
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    # Relation
    sensor_image_id = Column(Integer, ForeignKey("sensor_images.id"))
