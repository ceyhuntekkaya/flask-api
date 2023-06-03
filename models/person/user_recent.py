from db import db


class UserRecentModel(db.Model):
    __tablename__ = "user_recents"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)