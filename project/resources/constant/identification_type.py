from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.constant.identification_type import IdentificationTypeService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from db import db
from project.schemas.constant.identification_type import IdentificationTypeSchema

blp = Blueprint("IdentificationTypes", "identification_types", description="Operations on identification types")

main_route = "identification_type"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, IdentificationTypeSchema)
    def get(self, item_id):
        service = IdentificationTypeService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = IdentificationTypeService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(IdentificationTypeSchema)
    @blp.response(201, IdentificationTypeSchema)
    def put(self, item_data, item_id):
        service = IdentificationTypeService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, IdentificationTypeSchema(many=True))
    def get(self):
        service = IdentificationTypeService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(IdentificationTypeSchema)
    @blp.response(201, IdentificationTypeSchema)
    def post(self, item_data):
        service = IdentificationTypeService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
