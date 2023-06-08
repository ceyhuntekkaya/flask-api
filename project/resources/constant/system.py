from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.constant.system import SystemModel
from project.schemas.constant.system import SystemSchema

blp = Blueprint("Systems", "systems", description="Operations on systems")


@blp.route("/system/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, SystemSchema)
    def get(self, item_id):
        item = SystemModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = SystemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "System deleted"}, 200

    @blp.arguments(SystemSchema)
    @blp.response(201, SystemSchema)
    def put(self, item_data, item_id):
        item = SystemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = SystemModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/system")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, SystemSchema(many=True))
    def get(self):
        return SystemModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(SystemSchema)
    @blp.response(201, SystemSchema)
    def post(self, item_data):
        item = SystemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A system with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the system.")

        return item
