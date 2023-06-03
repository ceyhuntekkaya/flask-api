from db import db


class MarkerModel(db.Model):
    __tablename__ = "markers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)