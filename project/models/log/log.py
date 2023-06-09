from setting.db import db
from datetime import datetime

class LogModel(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    key = db.Column(db.String, nullable=False)
    log = db.Column(db.JSON)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    user_ip = db.Column(db.String, nullable=False)

