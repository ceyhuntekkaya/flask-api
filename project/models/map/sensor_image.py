from setting.db import db
from datetime import datetime

class SensorImageModel(db.Model):
    __tablename__ = "sensor_images"

    # Information
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.TEXT)
    image_order = db.Column(db.Integer)

    # Timing
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)

    # Relation
    sensor_id = db.Column(db.Integer, db.ForeignKey("sensors.id"))