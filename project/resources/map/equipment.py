from flask.views import MethodView
from flask_smorest import Blueprint, abort


from project.service.map.equipment import EquipmentService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.map.equipment import EquipmentSchema, EquipmentUpdateSchema
import os

blp = Blueprint("Equipments", "equipments", description="Operations on equipment")

APP_PATH = os.getenv("APP_PATH")
version = os.getenv("VERSION")
route = "equipment"
main_route = f"/{APP_PATH}/{version}/{route}"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    # @jwt_required()
    @blp.response(200, EquipmentSchema)
    def get(self, item_id):
        service = EquipmentService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    # @jwt_required()
    @blp.response(200, EquipmentSchema)
    def delete(self, item_id):
        service = EquipmentService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(EquipmentSchema)
    @blp.response(201, EquipmentSchema)
    def put(self, item_data, item_id):
        service = EquipmentService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    # @jwt_required()
    @blp.response(200, EquipmentSchema(many=True))
    def get(self):
        service = EquipmentService(db.session)
        return service.getAll()

    # @jwt_required(fresh=True)
    @blp.arguments(EquipmentSchema)
    @blp.response(201, EquipmentSchema)
    def post(self, item_data):
        service = EquipmentService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}/name/<string:name>")
class WithByName(MethodView):
    # @jwt_required()
    @blp.response(200, EquipmentSchema(many=True))
    def get(self, name):
        service = EquipmentService(db.session)
        return service.getByName(name)


@blp.route(f"/{main_route}/permanent/<string:item_id>")
class WithPermanent(MethodView):
    # @jwt_required()
    def delete(self, item_id):
        service = EquipmentService(db.session)
        item = service.permanent_delete(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return {"message": "Item deleted"}, 200


@blp.route(f"/{main_route}")
class UpdateWithId(MethodView):

    @blp.arguments(EquipmentSchema)
    @blp.response(201, EquipmentSchema)
    def put(self, item_data):
        service = EquipmentService(db.session)
        item = service.update(item_data, item_data["id"], 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


