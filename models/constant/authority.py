from db import db


class AuthorityModel(db.Model):
    __tablename__ = "authorities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)