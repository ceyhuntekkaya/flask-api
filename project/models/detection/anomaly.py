from setting.db import db
from datetime import datetime

class AnomalyModel(db.Model):
    __tablename__ = "anomalies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)

    latitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    anomaly_at = db.Column(db.TIMESTAMP, nullable=False)
    anomaly_level = db.Column(db.Integer, nullable=False)
    anomaly_color = db.Column(db.String, nullable=True)

    unique_id = db.Column(db.String, nullable=True)

    camera_id = db.Column(db.String, nullable=True)
    nvr_ip = db.Column(db.String, nullable=True)
    detector_name = db.Column(db.String, nullable=True)

    anomaly_type = db.Column(db.String, nullable=True)
    class_name = db.Column(db.String, nullable=True)
    confidence = db.Column(db.REAL, nullable=True)
    is_approved = db.Column(db.Integer, nullable=True)
    editable_description = db.Column(db.String, nullable=True)
    elevation = db.Column(db.REAL, nullable=True)

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

    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
