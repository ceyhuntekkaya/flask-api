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


class DetectionReportModel(db.Model):
    __tablename__ = "detection_reports"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    header = Column(String, nullable=False)
    content = Column(String, nullable=False)
    format = Column(String, nullable=False)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
