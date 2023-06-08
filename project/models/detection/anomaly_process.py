from db import db


class AnomalyProcessModel(db.Model):
    __tablename__ = "anomaly_process"

    id = db.Column(db.Integer, primary_key=True)
    anomaly_id = db.Column(db.Integer, db.ForeignKey("anomalies.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    process_at = db.Column(db.Integer)
    process = db.Column(db.String, nullable=False)

    create_at = db.Column(db.Integer)
    update_at = db.Column(db.Integer)
    delete_at = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)

    create_by = db.Column(db.Integer)
    update_by = db.Column(db.Integer)
    delete_by = db.Column(db.Integer)