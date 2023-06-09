from setting.db import db
from datetime import datetime

class ScreenshotModel(db.Model):
    __tablename__ = "screen_shots"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)

    latitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    begin_at = db.Column(db.TIMESTAMP, nullable=False)
    end_at = db.Column(db.TIMESTAMP, nullable=False)

    media_type = db.Column(db.String, unique=True, nullable=False)
    credential = db.Column(db.String)
    storage_address = db.Column(db.String)

    media_source_id = db.Column(db.Integer, db.ForeignKey("media_sources.id"), nullable=True)
    map_id = db.Column(db.Integer, db.ForeignKey("maps.id"), nullable=True)
    layer_id = db.Column(db.Integer, db.ForeignKey("layers.id"), nullable=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey("sensors.id"), nullable=True)
    unity_id = db.Column(db.Integer, db.ForeignKey("unities.id"), nullable=True)
    official_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    status = db.Column(db.String, unique=True, nullable=False)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer,nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
