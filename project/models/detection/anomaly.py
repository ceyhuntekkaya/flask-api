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
class AnomalyModel(db.Model):
    __tablename__ = "anomalies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(TEXT, unique=True, nullable=False)

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
    editable_description = Column(String, nullable=True)
    elevation = Column(REAL, nullable=True)

    map_id = Column(Integer, db.ForeignKey("maps.id"), nullable=True)
    layer_id = Column(Integer, db.ForeignKey("layers.id"), nullable=True)
    sensor_id = Column(Integer, db.ForeignKey("sensors.id"), nullable=True)
    unity_id = Column(Integer, db.ForeignKey("unities.id"), nullable=True)
    official_user_id = Column(Integer, db.ForeignKey("users.id"), nullable=True)
    status = Column(String, unique=True, nullable=False)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)
