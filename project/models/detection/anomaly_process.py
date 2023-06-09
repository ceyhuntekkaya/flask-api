from setting.db import db
from datetime import datetime

class AnomalyProcessModel(db.Model):
    __tablename__ = "anomaly_process"

    id = db.Column(db.Integer, primary_key=True)
    anomaly_id = db.Column(db.Integer, db.ForeignKey("anomalies.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    process_at = db.Column(db.TIMESTAMP)
    process = db.Column(db.String, nullable=False)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP)
    deleted_at = db.Column(db.TIMESTAMP)
    status = db.Column(db.Integer)

    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    deleted_by = db.Column(db.Integer)