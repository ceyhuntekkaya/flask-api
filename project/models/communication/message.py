from setting.db import db
from datetime import datetime


class MessageModel(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    
    header = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer)
    send_ip = db.Column(db.String)
    message_type = db.Column(db.String)

    message_from = db.Column(db.Integer, db.ForeignKey("users.id"))

    original_message_id = db.Column(db.Integer, db.ForeignKey("messages.id"), nullable=True)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    created_by = db.Column(db.Integer,nullable=True)

