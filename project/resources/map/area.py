from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.map.area import AreaService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.map.area import AreaSchema

blp = Blueprint("Areas", "areas", description="Operations on area")

main_route = "area"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AreaSchema)
    def get(self, item_id):
        service = AreaService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = AreaService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(AreaSchema)
    @blp.response(201, AreaSchema)
    def put(self, item_data, item_id):
        service = AreaService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AreaSchema(many=True))
    def get(self):
        service = AreaService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(AreaSchema)
    @blp.response(201, AreaSchema)
    def post(self, item_data):
        service = AreaService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
