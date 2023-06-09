from flask.views import MethodView
from flask_smorest import Blueprint, abort

from project.service.person.user import UserService
from json import JSONEncoder
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
)
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException

from setting.db import db
from project.schemas.person.user import UserSchema, UserLoginSchema, RegisterSchema
import os
from project.service.converters import convert_object

blp = Blueprint("Users", "users", description="Operations on user")

APP_PATH = os.getenv("APP_PATH")
version = os.getenv("VERSION")
route = "user"
main_route = f"/{APP_PATH}/{version}/{route}"


@blp.route(f"/{main_route}/name/<string:item_name>")
class WithName(MethodView):
    # @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self, item_name):
        service = UserService(db.session)
        item = service.getByName(item_name)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    # @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, item_id):
        service = UserService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    # @jwt_required()
    @blp.response(200, UserSchema)
    def delete(self, item_id):
        service = UserService(db.session)
        item = service.delete(item_id, 1)
        print(item)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def put(self, item_data, item_id):
        service = UserService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    # @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        service = UserService(db.session)
        return service.getAll()

    # @jwt_required(fresh=True)


@blp.route("/auth/register")
class UserRegister(MethodView):
    @blp.arguments(RegisterSchema)
    @blp.response(200, UserSchema)
    def post(self, item_data):
        service = UserService(db.session)
        item = service.add(item_data, 1)
        print(item)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        item_created = service.getById(item)
        return item_created


@blp.route("/auth/login")
class UserLogin(MethodView):
    @blp.arguments(UserLoginSchema)
    def post(self, item_data):
        service = UserService(db.session)
        item = service.getByUsername(item_data["username"], item_data["password"])
        if type(item) == EntityNotFoundException:
            abort(401, message="Invalid credentials.")
        access_token = create_access_token(identity=item.id, fresh=True)
        refresh_token = create_refresh_token(item.id)
        item_converted = convert_object(item)
        return {"user": item_converted,
                "user_preferences": {},
                "user_authorities": {},
                "user_recent": {},
                "user_role": {},
                "user_hierarchy": {},
                "user_command": {},
                "user_command_collar_mark": {},
                "user_command_collar_mark_rank": {},
                "access_token": access_token,
                "refresh_token": refresh_token}, 200


@blp.route(f"/{main_route}/permanent/<string:item_id>")
class PermanentDelete(MethodView):
    # @jwt_required()
    @blp.response(200, UserSchema)
    def delete(self, item_id):
        service = UserService(db.session)
        item = service.permanent_delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}/active")
class AllActives(MethodView):
    # @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        service = UserService(db.session)
        return service.getActive()
