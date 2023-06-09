from setting.db import db
from datetime import datetime

class UserAuthorityModel(db.Model):
    __tablename__ = "user_authorities"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    authority_type = db.Column(db.String, unique=False, nullable=True)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer,nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)

    authority_id = db.Column(db.Integer, db.ForeignKey("authorities.id"))
