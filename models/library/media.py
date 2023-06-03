from db import db


class MediaModel(db.Model):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)