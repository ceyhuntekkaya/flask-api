from setting.db import db


class SensorImageModel(db.Model):
    __tablename__ = "sensor_images"

    # Information
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.TEXT)
    image_order = db.Column(db.Integer)

    # Timing
    create_at = db.Column(db.Integer, nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)

    # Relation
    sensor_id = db.Column(db.Integer, db.ForeignKey("sensors.id"))