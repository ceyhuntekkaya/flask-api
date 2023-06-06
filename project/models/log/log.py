from db import db


class LogModel(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    event_type = db.Column(db.String, nullable=False)
    event_at = db.Column(db.String, nullable=False)
    user_ip = db.Column(db.String, nullable=False)
    unity_id = db.Column(db.Integer, db.ForeignKey("unities.id"), nullable=True)
    description = db.Column(db.String, nullable=True)
