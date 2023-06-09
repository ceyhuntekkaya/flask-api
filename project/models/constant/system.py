from setting.db import db
from datetime import datetime


class SystemModel(db.Model):
    __tablename__ = "aselsan_system"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, default=1)

    system_status = db.Column(db.Enum("training", "live", "standby", name="SystemStatusEnum"), default="standby")

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)