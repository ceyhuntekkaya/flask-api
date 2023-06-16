from flask.views import MethodView
from flask_smorest import Blueprint, abort

from project.schemas.map.unit_layer import LayerTreeSchema
from project.service.map.layer import LayerService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.map.layer import LayerSchema, LayerCreateSchema, PlainLayerSchema, LayerUpdateSchema

import os

blp = Blueprint("Layers", "layers", description="Operations on layer")

APP_PATH = os.getenv("APP_PATH")
version = os.getenv("VERSION")
route = "layer"
main_route = f"/{APP_PATH}/{version}/{route}"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    # @jwt_required()
    @blp.response(200, LayerSchema)
    def get(self, item_id):
        service = LayerService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    # @jwt_required()
    @blp.response(200, LayerSchema)
    def delete(self, item_id):
        service = LayerService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    # @jwt_required()
    @blp.response(200, LayerSchema(many=True))
    def get(self):
        service = LayerService(db.session)
        return service.getAll()

    # @jwt_required(fresh=True)
    @blp.arguments(LayerCreateSchema)
    @blp.response(201, PlainLayerSchema)
    def post(self, item_data):
        service = LayerService(db.session)
        item = service.add(item_data)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(LayerUpdateSchema)
    @blp.response(201, LayerSchema)
    def put(self, item_data):
        service = LayerService(db.session)
        item = service.update(item_data, item_data["updated_by"])
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}/name/<string:name>")
class WithByName(MethodView):
    # @jwt_required()
    @blp.response(200, LayerSchema(many=True))
    def get(self, name):
        service = LayerService(db.session)
        return service.getByName(name)


@blp.route(f"/{main_route}/tree/<string:item_id>")
class WithByName(MethodView):
    # @jwt_required()
    @blp.response(200, LayerTreeSchema())
    def get(self, item_id):
        service = LayerService(db.session)
        return service.getLayerTree(item_id)


@blp.route(f"/{main_route}/permanent/<string:item_id>")
class WithPermanent(MethodView):
    # @jwt_required()
    def delete(self, item_id):
        service = LayerService(db.session)
        item = service.permanent_delete(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return {"message": "Item deleted"}, 200

