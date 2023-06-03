from db import db


class ScreenshotModel(db.Model):
    __tablename__ = "screen_shots"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)