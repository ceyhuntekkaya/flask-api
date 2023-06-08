from setting.db import db
from project.models.base_model import BaseModelClass


class UserModel(db.Model, BaseModelClass):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    surname = db.Column(db.String, unique=False, nullable=False)
    registration_number = db.Column(db.String, unique=True, nullable=True)
    phone = db.Column(db.String, unique=False, nullable=True)
    mail = db.Column(db.String, unique=True, nullable=True)
    code = db.Column(db.String, unique=False, nullable=True)
    phone_extension_line = db.Column(db.String, unique=False, nullable=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
    last_login = db.Column(db.Integer,nullable=True)
    last_login_ip = db.Column(db.String, unique=False, nullable=True)

    role_id = db.Column(
        db.Integer, db.ForeignKey("roles.id"), unique=False, nullable=True
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
        db.Integer, db.ForeignKey("command_collar_mark_ranks.id"), unique=False, nullable=False
    )

