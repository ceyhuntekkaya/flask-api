from setting.db import db


class SensorImagePointModel(db.Model):
    __tablename__ = "sensor_image_points"

    # Information
    id = db.Column(db.Integer, primary_key=True)

    points = db.Column(db.JSON)

    # Timing
    create_at = db.Column(db.Integer, nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)

    # Relation
    sensor_id = db.Column(db.Integer, db.ForeignKey("aselsan_sensors.id"))