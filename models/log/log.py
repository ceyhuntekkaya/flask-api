from db import db


class LogModel(db.Model):
    __tablename__ = "kogs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)