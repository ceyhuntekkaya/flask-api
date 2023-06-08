from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.constant.command import CommandService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.constant.command import CommandSchema

blp = Blueprint("Command", "commands", description="Operations on command")

main_route = "command"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, CommandSchema)
    def get(self, item_id):
        service = CommandService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = CommandService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(CommandSchema)
    @blp.response(201, CommandSchema)
    def put(self, item_data, item_id):
        service = CommandService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, CommandSchema(many=True))
    def get(self):
        service = CommandService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(CommandSchema)
    @blp.response(201, CommandSchema)
    def post(self, item_data):
        service = CommandService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
