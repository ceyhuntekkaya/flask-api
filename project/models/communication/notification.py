from setting.db import db
from datetime import datetime


class NotificationModel(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    
    header = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer)
    send_ip = db.Column(db.String)
    notification_type = db.Column(db.String)

    notification_from = db.Column(db.Integer, db.ForeignKey("users.id"))

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    created_by = db.Column(db.Integer,nullable=True)
