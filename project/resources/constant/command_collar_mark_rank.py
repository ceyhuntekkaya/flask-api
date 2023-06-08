from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.constant.command_collar_mark_rank import CommandCollarMarkRankService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from db import db
from project.schemas.constant.command_collar_mark_rank import CommandCollarMarkRankSchema

blp = Blueprint("CommandCollarMarkRanks", "command_collar_mark_ranks",
                description="Operations on command collar mark rank")

main_route = "command_collar_mark_rank"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, CommandCollarMarkRankSchema)
    def get(self, item_id):
        service = CommandCollarMarkRankService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = CommandCollarMarkRankService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(CommandCollarMarkRankSchema)
    @blp.response(201, CommandCollarMarkRankSchema)
    def put(self, item_data, item_id):
        service = CommandCollarMarkRankService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, CommandCollarMarkRankSchema(many=True))
    def get(self):
        service = CommandCollarMarkRankService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(CommandCollarMarkRankSchema)
    @blp.response(201, CommandCollarMarkRankSchema)
    def post(self, item_data):
        service = CommandCollarMarkRankService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
