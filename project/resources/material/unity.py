from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.material.unity import UnityModel
from project.schemas.material.unity import UnitySchema

blp = Blueprint("Unities", "unitys", description="Operations on unity")


@blp.route("/unity/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, UnitySchema)
    def get(self, item_id):
        item = UnityModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = UnityModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Unity deleted"}, 200

    @blp.arguments(UnitySchema)
    @blp.response(201, UnitySchema)
    def put(self, item_data, item_id):
        item = UnityModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = UnityModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/unity")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, UnitySchema(many=True))
    def get(self):
        return UnityModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(UnitySchema)
    @blp.response(201, UnitySchema)
    def post(self, item_data):
        item = UnityModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A unity with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the unity.")

        return item
