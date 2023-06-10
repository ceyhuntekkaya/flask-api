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


class MessageToListModel(db.Model):
    __tablename__ = "message_to_list"

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, db.ForeignKey("messages.id"))
    read_at = Column(TIMESTAMP, nullable=True)
    read_ip = Column(String)
    

