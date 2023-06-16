from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.map.sensor import SensorService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.map.sensor import SensorSchema
import os

blp = Blueprint("Sensors", "sensors", description="Operations on sensor")

APP_PATH = os.getenv("APP_PATH")
version = os.getenv("VERSION")
route = "sensor"
main_route = f"/{APP_PATH}/{version}/{route}"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    # @jwt_required()
    @blp.response(200, SensorSchema)
    def get(self, item_id):
        service = SensorService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    # @jwt_required()
    @blp.response(200, SensorSchema)
    def delete(self, item_id):
        service = SensorService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}/name/<string:name>")
class WithByName(MethodView):
    # @jwt_required()
    @blp.response(200, SensorSchema(many=True))
    def get(self, name):
        service = SensorService(db.session)
        return service.getByName(name)


@blp.route(f"/{main_route}")
class Plain(MethodView):
    # @jwt_required()
    @blp.response(200, SensorSchema(many=True))
    def get(self):
        service = SensorService(db.session)
        return service.getAll()

    # @jwt_required(fresh=True)
    @blp.arguments(SensorSchema)
    @blp.response(201, SensorSchema)
    def post(self, item_data):
        service = SensorService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(SensorSchema)
    @blp.response(201, SensorSchema)
    def put(self, item_data):
        service = SensorService(db.session)
        item = service.update(item_data, item_data["id"], 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}/permanent/<string:item_id>")
class WithPermanent(MethodView):
    # @jwt_required()
    def delete(self, item_id):
        service = SensorService(db.session)
        item = service.permanent_delete(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return {"message": "Item deleted"}, 200
