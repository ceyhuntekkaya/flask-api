from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.log.log import LogService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from db import db
from project.schemas.log.log import LogSchema

blp = Blueprint("Logs", "logs", description="Operations on log")

main_route = "log"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, LogSchema)
    def get(self, item_id):
        service = LogService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = LogService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(LogSchema)
    @blp.response(201, LogSchema)
    def put(self, item_data, item_id):
        service = LogService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, LogSchema(many=True))
    def get(self):
        service = LogService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(LogSchema)
    @blp.response(201, LogSchema)
    def post(self, item_data):
        service = LogService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
