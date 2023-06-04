from db import db


class CommandCollarMarkRankModel(db.Model):
    __tablename__ = "command_collar_mark_rakss"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    hierarchical_order = db.Column(db.Integer, unique=True, nullable=False)
    command_collar_mark_id = db.Column(
        db.Integer, db.ForeignKey("command_collar_marks.id"), unique=False, nullable=False
    )



    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
