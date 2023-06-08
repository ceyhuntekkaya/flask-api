from setting.db import db


class AnomalyNoteModel(db.Model):
    __tablename__ = "anomaly_notes"

    id = db.Column(db.Integer, primary_key=True)
    anomaly_id = db.Column(db.Integer, db.ForeignKey("anomalies.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    note_at = db.Column(db.Integer)
    content = db.Column(db.String, nullable=False)

    create_at = db.Column(db.Integer)
    update_at = db.Column(db.Integer)
    delete_at = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)

    create_by = db.Column(db.Integer)
    update_by = db.Column(db.Integer)
    delete_by = db.Column(db.Integer)