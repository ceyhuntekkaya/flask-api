from setting.db import db
from datetime import datetime

class AnomalyNoteModel(db.Model):
    __tablename__ = "anomaly_notes"

    id = db.Column(db.Integer, primary_key=True)
    anomaly_id = db.Column(db.Integer, db.ForeignKey("anomalies.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    note_at = db.Column(db.TIMESTAMP)
    content = db.Column(db.String, nullable=False)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP)
    deleted_at = db.Column(db.TIMESTAMP)
    status = db.Column(db.Integer)

    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    deleted_by = db.Column(db.Integer)