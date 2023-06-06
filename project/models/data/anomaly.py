from datetime import datetime

from sqlalchemy import (
    REAL,
    TEXT,
    TIMESTAMP,
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base
from project.models.base_model import BaseModelClass

Base = declarative_base()


class Anomaly(Base, BaseModelClass):
    __tablename__ = "aselsan_anomaly"

    id = Column(Integer, primary_key=True)

    # Information
    status = Column(Integer, default=1)
    anomaly_type = Column(String)
    class_name = Column(String)
    confidence = Column(REAL)
    is_approved = Column(Integer)
    description = Column(TEXT)
    editable_description = Column(TEXT)

    # Geographic information
    lat = Column(REAL)
    lon = Column(REAL)
    elevation = Column(REAL)

    # Device information
    unique_id = Column(String)
    sensor_id = Column(Integer)
    unit_id = Column(Integer)
    camera_id = Column(String)
    nvr_ip = Column(String)
    detector_name = Column(String)

    # System timing
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
