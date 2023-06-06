from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.material.sensor import SensorModel
from project.schemas.material.sensor import SensorSchema

blp = Blueprint("Sensors", "sensors", description="Operations on sensor")


@blp.route("/sensor/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, SensorSchema)
    def get(self, item_id):
        item = SensorModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = SensorModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Sensor deleted"}, 200

    @blp.arguments(SensorSchema)
    @blp.response(201, SensorSchema)
    def put(self, item_data, item_id):
        item = SensorModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = SensorModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/sensor")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, SensorSchema(many=True))
    def get(self):
        return SensorModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(SensorSchema)
    @blp.response(201, SensorSchema)
    def post(self, item_data):
        item = SensorModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A sensor with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the sensor.")

        return item
