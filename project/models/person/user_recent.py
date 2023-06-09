from setting.db import db
from datetime import datetime

class UserRecentModel(db.Model):
    __tablename__ = "user_recent"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, unique=False, nullable=True)
    value = db.Column(db.String, unique=False, nullable=True)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer,nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
