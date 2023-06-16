from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.map.area import AreaService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.map.area import AreaSchema, AreaCreateSchema, AreaUpdateSchema
import os

blp = Blueprint("Areas", "areas", description="Operations on area")

APP_PATH = os.getenv("APP_PATH")
version = os.getenv("VERSION")
route = "area"
main_route = f"/{APP_PATH}/{version}/{route}"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    # @jwt_required()
    @blp.response(200, AreaSchema)
    def get(self, item_id):
        service = AreaService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    # @jwt_required()
    @blp.response(200, AreaSchema)
    def delete(self, item_id):
        service = AreaService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    # @jwt_required()
    @blp.response(200, AreaSchema(many=True))
    def get(self):
        service = AreaService(db.session)
        return service.getAll()

    # @jwt_required(fresh=True)
    @blp.arguments(AreaCreateSchema)
    @blp.response(201, AreaSchema)
    def post(self, item_data):
        service = AreaService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(AreaUpdateSchema)
    @blp.response(201, AreaSchema)
    def put(self, item_data):
        service = AreaService(db.session)
        item = service.update(item_data, item_data["area"]["id"], item_data["area"]["updated_by"])
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item




@blp.route(f"/{main_route}/name/<string:name>")
class WithByName(MethodView):
    # @jwt_required()
    @blp.response(200, AreaSchema(many=True))
    def get(self, name):
        service = AreaService(db.session)
        return service.getByName(name)


@blp.route(f"/{main_route}/permanent/<string:item_id>")
class WithPermanent(MethodView):
    # @jwt_required()
    def delete(self, item_id):
        service = AreaService(db.session)
        item = service.permanent_delete(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return {"message": "Item deleted"}, 200
