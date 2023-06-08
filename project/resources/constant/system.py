from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.constant.system import SystemService

from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException

from db import db
from project.schemas.constant.system import SystemSchema

blp = Blueprint("Systems", "systems", description="Operations on systems")

main_route = "system"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, SystemSchema)
    def get(self, item_id):
        service = SystemService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = SystemService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(SystemSchema)
    @blp.response(201, SystemSchema)
    def put(self, item_data, item_id):
        service = SystemService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, SystemSchema(many=True))
    def get(self):
        service = SystemService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(SystemSchema)
    @blp.response(201, SystemSchema)
    def post(self, item_data):
        service = SystemService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
