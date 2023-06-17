from flask.views import MethodView
from flask_smorest import Blueprint, abort

from project.schemas.map.unit_layer import LayerTreeSchema, UnitWithLayerSchema
from project.service.map.unit import UnitService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.map.unit import UnitSchema, UnitUpdateSchema
import os

blp = Blueprint("Units", "unites", description="Operations on unit")

APP_PATH = os.getenv("APP_PATH")
version = os.getenv("VERSION")
route = "unit"
main_route = f"/{APP_PATH}/{version}/{route}"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    # @jwt_required()
    @blp.response(200, UnitSchema)
    def get(self, item_id):
        service = UnitService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    # @jwt_required()
    @blp.response(200, UnitSchema)
    def delete(self, item_id):
        service = UnitService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(UnitUpdateSchema)
    @blp.response(201, UnitSchema)
    def put(self, item_data, item_id):
        service = UnitService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    # @jwt_required()
    @blp.response(200, UnitSchema(many=True))
    def get(self):
        service = UnitService(db.session)
        return service.getAll()

    # @jwt_required(fresh=True)
    @blp.arguments(UnitSchema)
    @blp.response(201, UnitSchema)
    def post(self, item_data):
        service = UnitService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}/name/<string:name>")
class WithByName(MethodView):
    # @jwt_required()
    @blp.response(200, UnitSchema(many=True))
    def get(self, name):
        service = UnitService(db.session)
        return service.getByName(name)


@blp.route(f"/{main_route}/permanent/<string:item_id>")
class WithPermanent(MethodView):
    # @jwt_required()
    def delete(self, item_id):
        service = UnitService(db.session)
        item = service.permanent_delete(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return {"message": "Item deleted"}, 200


@blp.route(f"/{main_route}")
class UpdateWithId(MethodView):

    @blp.arguments(UnitUpdateSchema)
    @blp.response(201, UnitSchema)
    def put(self, item_data):
        service = UnitService(db.session)
        item = service.update(item_data, item_data["id"], 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}/tree/<string:item_id>")
class WithTree(MethodView):
    # @jwt_required()
    @blp.response(200, LayerTreeSchema())
    def get(self, name):
        service = UnitService(db.session)
        return service.getByName(name)


@blp.route(f"/{main_route}/recursive")
class WithByRecursive(MethodView):
    # @jwt_required()

    def get(self):
        service = UnitService(db.session)
        return service.getRecursive()


@blp.route(f"/{main_route}/layer/<string:item_id>")
class WithByName(MethodView):
    # @jwt_required()
    @blp.response(200, UnitWithLayerSchema(many=True))
    def get(self, item_id):
        service = UnitService(db.session)
        return service.getLayers(item_id)
