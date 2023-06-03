from db import db


class UserRecentModel(db.Model):
    __tablename__ = "user_recents"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, unique=False, nullable=True)
    value = db.Column(db.String, unique=False, nullable=True)