from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.constant.role import RoleModel
from schemas.constant.role import RoleSchema, PlainRoleSchema


blp = Blueprint("Roles", "roles", description="Operations on roles")


@blp.route("/role")
class RoleRegister(MethodView):
    @blp.arguments(RoleSchema)
    def post(self, role_data):
        role = RoleModel(**role_data)
        try:
            db.session.add(role)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A role with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the role.")

        return role
