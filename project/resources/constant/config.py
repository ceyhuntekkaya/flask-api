from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.constant.config import ConfigModel
from project.schemas.constant.config import ConfigSchema

blp = Blueprint("Configs", "configs", description="Operations on configs")


@blp.route("/config/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, ConfigSchema)
    def get(self, item_id):
        item = ConfigModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = ConfigModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Config deleted"}, 200

    @blp.arguments(ConfigSchema)
    @blp.response(201, ConfigSchema)
    def put(self, item_data, item_id):
        item = ConfigModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ConfigModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/config")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, ConfigSchema(many=True))
    def get(self):
        return ConfigModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(ConfigSchema)
    @blp.response(201, ConfigSchema)
    def post(self, item_data):
        item = ConfigModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A config with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the config.")

        return item
