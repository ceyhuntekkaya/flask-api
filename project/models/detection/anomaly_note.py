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
class AnomalyNoteModel(db.Model):
    __tablename__ = "anomaly_notes"

    id = Column(Integer, primary_key=True)
    anomaly_id = Column(Integer, db.ForeignKey("anomalies.id"))
    user_id = Column(Integer, db.ForeignKey("users.id"))
    note_at = Column(TIMESTAMP)
    content = Column(String, nullable=False)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
    status = Column(Integer)

    created_by = Column(Integer)
    updated_by = Column(Integer)
    deleted_by = Column(Integer)