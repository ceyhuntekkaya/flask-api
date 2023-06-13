from setting.db import db
from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
)


class NotificationToListModel(db.Model):
    __tablename__ = "notification_to_list"

    id = Column(Integer, primary_key=True)
    notification_id = Column(Integer, ForeignKey("notifications.id"))
    read_at = Column(TIMESTAMP, nullable=True)
    read_ip = Column(String)
