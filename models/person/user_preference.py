from db import db


class UserPreferenceModel(db.Model):
    __tablename__ = "user_preferences"

    id = db.Column(db.Integer, primary_key=True)
    preference_id = db.Column(db.Integer, db.ForeignKey("preferences.id"))
    value = db.Column(db.String, unique=False, nullable=True)