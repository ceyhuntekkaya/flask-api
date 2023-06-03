from db import db


class DetectionReportModel(db.Model):
    __tablename__ = "detection_reports"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)