from db import db


class DetectionModel(db.Model):
    __tablename__ = "detections"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)