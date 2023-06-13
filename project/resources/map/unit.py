from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.map.unit import UnitService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.map.unit import UnitSchema

blp = Blueprint("Units", "unites", description="Operations on unit")

main_route = "unit"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, UnitSchema)
    def get(self, item_id):
        service = UnitService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = UnitService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(UnitSchema)
    @blp.response(201, UnitSchema)
    def put(self, item_data, item_id):
        service = UnitService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, UnitSchema(many=True))
    def get(self):
        service = UnitService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(UnitSchema)
    @blp.response(201, UnitSchema)
    def post(self, item_data):
        service = UnitService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
