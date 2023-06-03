from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(80), unique=False, nullable=False)
    # command = db.Column(db.String(80), unique=False, nullable=True)
    # collar_mark = db.Column(db.String(80), unique=False, nullable=True)
    # rank = db.Column(db.String(80), unique=False, nullable=True)
    registration_number = db.Column(db.String(80), unique=True, nullable=True)
    phone = db.Column(db.String(80), unique=False, nullable=True)
    mail = db.Column(db.String(80), unique=True, nullable=True)
    code = db.Column(db.String(80), unique=False, nullable=True)
    phone_extension_line = db.Column(db.String(80), unique=False, nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    active = db.Column(db.Boolean, nullable=True)

    role_id = db.Column(
        db.Integer, db.ForeignKey("roles.id"), unique=False, nullable=False
    )
    hierarchy_id = db.Column(
        db.Integer, db.ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    command_id = db.Column(
        db.Integer, db.ForeignKey("commands.id"), unique=False, nullable=False
    )
    command_collar_mark_id = db.Column(
        db.Integer, db.ForeignKey("command_collar_marks.id"), unique=False, nullable=False
    )
    command_collar_mark_rank_id = db.Column(
        db.Integer, db.ForeignKey("command_collar_mark_rakss.id"), unique=False, nullable=False
    )
