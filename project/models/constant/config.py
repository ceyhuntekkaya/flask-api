from setting.db import db
from datetime import datetime


class ConfigModel(db.Model):
    __tablename__ = "aselsan_config"

    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.Integer, default=1)
    config_json = db.Column(db.JSON)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
