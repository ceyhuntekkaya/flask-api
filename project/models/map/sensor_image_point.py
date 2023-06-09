from setting.db import db
from datetime import datetime

class SensorImagePointModel(db.Model):
    __tablename__ = "sensor_image_points"

    # Information
    id = db.Column(db.Integer, primary_key=True)

    points = db.Column(db.JSON)

    # Timing
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)

    # Relation
    sensor_id = db.Column(db.Integer, db.ForeignKey("aselsan_sensors.id"))