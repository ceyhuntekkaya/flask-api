from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TEXT,
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
)


class NotificationModel(db.Model):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)

    header = Column(String, nullable=False)
    content = Column(TEXT, nullable=False)
    priority = Column(Integer)
    send_ip = Column(String)
    notification_type = Column(String)

    notification_from = Column(Integer, ForeignKey("users.id"))

    created_at = Column(TIMESTAMP, default=datetime.now())
    deleted_at = Column(TIMESTAMP, nullable=True)
    created_by = Column(Integer, nullable=True)
