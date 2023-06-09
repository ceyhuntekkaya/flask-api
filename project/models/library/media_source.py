from setting.db import db
from datetime import datetime

class MediaSourceModel(db.Model):
    __tablename__ = "media_sources"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    latitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    credential = db.Column(db.String)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer,nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)