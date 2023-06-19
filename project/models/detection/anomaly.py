from setting.db import db
from datetime import datetime
from sqlalchemy import (
    REAL,
    TEXT,
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
)


class AnomalyModel(db.Model):
    __tablename__ = "anomalies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(TEXT)

    latitude = Column(Float(precision=5), unique=False, nullable=False)
    longitude = Column(Float(precision=5), unique=False, nullable=False)
    anomaly_at = Column(TIMESTAMP, nullable=False)
    anomaly_level = Column(Integer, nullable=False)
    anomaly_color = Column(String, nullable=True)

    unique_id = Column(String, nullable=True)

    camera_id = Column(String, nullable=True)
    nvr_ip = Column(String, nullable=True)
    detector_name = Column(String, nullable=True)

    anomaly_type = Column(String, nullable=True)
    class_name = Column(String, nullable=True)
    confidence = Column(REAL, nullable=True)
    is_approved = Column(Integer, nullable=True)
    editable_description = Column(TEXT)
    elevation = Column(REAL, nullable=True)

    layer_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    area_id = Column(Integer, ForeignKey("areas.id"), nullable=True)
    sensor_id = Column(Integer, ForeignKey("sensors.id"), nullable=True)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=True)
    status = Column(String, nullable=False)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
