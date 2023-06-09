from setting.db import db
from datetime import datetime

class DetectionReportModel(db.Model):
    __tablename__ = "detection_reports"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    header = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    format = db.Column(db.String, nullable=False)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer,nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
