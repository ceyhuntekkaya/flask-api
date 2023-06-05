from db import db


class DetectionRouteModel(db.Model):
    __tablename__ = "detection_routes"

    id = db.Column(db.Integer, primary_key=True)
    detection_id = db.Column(db.Integer, db.ForeignKey("detections.id"))

    latitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)
    detection_at = db.Column(db.Integer, nullable=False)
    anomaly_level = db.Column(db.Integer, nullable=False)
    create_at = db.Column(db.Integer)
    delete_at = db.Column(db.Integer)
    delete_by = db.Column(db.Integer)
