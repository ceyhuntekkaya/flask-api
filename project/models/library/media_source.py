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
class MediaSourceModel(db.Model):
    __tablename__ = "media_sources"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    latitude = Column(Float(precision=5), unique=False, nullable=False)
    longitude = Column(Float(precision=5), unique=False, nullable=False)
    credential = Column(String)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(Integer,nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)