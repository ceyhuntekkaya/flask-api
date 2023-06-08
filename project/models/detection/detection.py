from setting.db import db


class DetectionModel(db.Model):
    __tablename__ = "detections"

    id = db.Column(db.Integer, primary_key=True)
    detection_start_time = db.Column(db.TIMESTAMP)
    detection_lat = db.Column(db.REAL)
    detection_lon = db.Column(db.REAL)

