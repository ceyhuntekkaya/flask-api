from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.constant.role import RoleModel
from schemas.constant.role import RoleSchema


blp = Blueprint("Roles", "roles", description="Operations on roles")


@blp.route("/role/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, RoleSchema)
    def get(self, item_id):
        item = RoleModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = RoleModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Role deleted"}, 200

     
    @blp.arguments(RoleSchema)
    @blp.response(201, RoleSchema)
    def put(self, item_data, item_id):
        item = RoleModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = RoleModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/role")
class Plain(MethodView):
    @blp.response(200, RoleSchema(many=True))
    def get(self):
        return RoleModel.query.all()

    @blp.arguments(RoleSchema)
    @blp.response(201, RoleSchema)
    def post(self, item_data):
        item = RoleModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A role with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the role.")

        return item
    
