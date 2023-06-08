from setting.db import db


class LogModel(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    key = db.Column(db.String, nullable=False)
    log = db.Column(db.JSON)
    created_at = db.Column(db.Integer)
    user_ip = db.Column(db.String, nullable=False)

