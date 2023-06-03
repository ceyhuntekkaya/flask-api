from db import db


class PreferenceModel(db.Model):
    __tablename__ = "preferences"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)