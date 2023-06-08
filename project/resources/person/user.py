from flask.views import MethodView
from flask_smorest import Blueprint, abort

from project.service.person.user import UserService

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
)
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException

from db import db
from project.models.person.user import UserModel
from project.schemas.person.user import UserSchema, UserLoginSchema

blp = Blueprint("Users", "users", description="Operations on user")

main_route = "user"


@blp.route(f"/{main_route}/name/<string:item_name>")
class WithName(MethodView):
    # @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self, item_name):
        service = UserService(db.session)
        return service.getByName(item_name)


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

    @jwt_required()
    def delete(self, item_id):
        service = UserService(db.session)
        item = service.delete(item_id, 1)
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

        item = UserModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = UserModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    # @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        service = UserService(db.session)
        return service.getAll()

    # @jwt_required(fresh=True)


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, item_data):
        service = UserService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserLoginSchema)
    def post(self, item_data):
        service = UserService(db.session)
        item = service.getByUsername(item_data["username"], item_data["password"])
        if type(item) == EntityNotFoundException:
            abort(401, message="Invalid credentials.")
        access_token = create_access_token(identity=item.id, fresh=True)
        refresh_token = create_refresh_token(item.id)
        return {"user": item,
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
