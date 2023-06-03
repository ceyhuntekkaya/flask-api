from db import db


class DetectionReportModel(db.Model):
    __tablename__ = "detection_reports"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)