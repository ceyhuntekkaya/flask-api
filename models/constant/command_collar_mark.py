from db import db


class CommandCollarMarkModel(db.Model):
    __tablename__ = "command_collar_marks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    hierarchical_order = db.Column(db.Integer, unique=True, nullable=False)
    command_id = db.Column(
        db.Integer, db.ForeignKey("commands.id"), unique=False, nullable=False
    )