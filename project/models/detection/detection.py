from setting.db import db

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
class DetectionModel(db.Model):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True)
    detection_start_time = Column(TIMESTAMP)
    detection_lat = Column(REAL)
    detection_lon = Column(REAL)

