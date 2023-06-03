from db import db


class UserAuthorityModel(db.Model):
    __tablename__ = "user_authorities"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    authority_id = db.Column(db.Integer, db.ForeignKey("authorities.id"))
    authority_type = db.Column(db.String(80), unique=False, nullable=True)