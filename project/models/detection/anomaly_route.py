from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TEXT,
    TIMESTAMP,
    Column,
    Integer,
    ForeignKey,
    Float,
)


class AnomalyRouteModel(db.Model):
    __tablename__ = "anomaly_routes"

    id = Column(Integer, primary_key=True)
    anomaly_id = Column(Integer, ForeignKey("anomalies.id"))

    lat = Column(Float(precision=5), unique=False, nullable=False)
    lon = Column(Float(precision=5), unique=False, nullable=False)
    description = Column(TEXT)
    anomaly_level = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    deleted_at = Column(TIMESTAMP)
    deleted_by = Column(Integer)
