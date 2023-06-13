from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TIMESTAMP,
    Column,
    TEXT,
    Integer,
    String,
    ForeignKey,
)


class MessageModel(db.Model):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)

    header = Column(String, nullable=False)
    content = Column(TEXT, nullable=False)
    priority = Column(Integer)
    send_ip = Column(String)
    message_type = Column(String)

    message_from = Column(Integer, ForeignKey("users.id"))

    original_message_id = Column(Integer, ForeignKey("messages.id"), nullable=True)

    created_at = Column(TIMESTAMP, default=datetime.now())
    deleted_at = Column(TIMESTAMP, nullable=True)
    created_by = Column(Integer, nullable=True)
