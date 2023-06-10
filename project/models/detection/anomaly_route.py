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
class AnomalyRouteModel(db.Model):
    __tablename__ = "anomaly_routes"

    id = Column(Integer, primary_key=True)
    anomaly_id = Column(Integer, db.ForeignKey("anomalies.id"))

    latitude = Column(Float(precision=5), unique=False, nullable=False)
    longitude = Column(Float(precision=5), unique=False, nullable=False)
    description = Column(String, unique=True, nullable=False)
    anomaly_level = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    deleted_at = Column(TIMESTAMP)
    deleted_by = Column(Integer)
