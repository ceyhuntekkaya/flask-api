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
class MarkerModel(db.Model):
    __tablename__ = "markers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)

    type = Column(String, unique=False, nullable=False)
    color = Column(String, unique=False, nullable=False)

    sensor_id = Column(Integer, ForeignKey("maps.id"), nullable=True)
    sign_id = Column(Integer, ForeignKey("maps.id"), nullable=True)
    symbol_id = Column(Integer, ForeignKey("maps.id"), nullable=True)
    unity_id = Column(Integer, ForeignKey("maps.id"), nullable=True)

    description = Column(String)
    latitude = Column(Float(precision=5), unique=False, nullable=False)
    longitude = Column(Float(precision=5), unique=False, nullable=False)

    map_id = Column(Integer, ForeignKey("maps.id"), nullable=True)
    layer_id = Column(Integer, ForeignKey("layers.id"), nullable=True)
    hierarchy_id = Column(
        Integer, ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    official_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)
