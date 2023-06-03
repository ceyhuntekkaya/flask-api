from db import db


class CommandModel(db.Model):
    __tablename__ = "commands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    hierarchical_order = db.Column(db.Integer, unique=True, nullable=False)