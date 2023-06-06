from db import db


class UserRecentModel(db.Model):
    __tablename__ = "user_recents"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, unique=False, nullable=True)
    value = db.Column(db.String, unique=False, nullable=True)

    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
