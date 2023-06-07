from flask.views import MethodView
from flask_smorest import Blueprint, abort

from project.service.person.user import UserService

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
)

from db import db
from project.models.person.user import UserModel
from project.schemas.person.user import UserSchema, UserLoginSchema
from passlib.hash import pbkdf2_sha256

blp = Blueprint("Users", "users", description="Operations on user")


@blp.route("/user/name/<string:item_name>")
class WithName(MethodView):
    # @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self, item_name):
        service = UserService(db.session)
        return service.getByName(item_name)


@blp.route("/user/<string:item_id>")
class WithId(MethodView):
    # @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, item_id):
        service = UserService(db.session)
        return service.getById(item_id)

    @jwt_required()
    def delete(self, item_id):
        service = UserService(db.session)
        return service.delete(item_id)

        item = UserModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "User deleted"}, 200

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def put(self, item_data, item_id):
        item = UserModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = UserModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()
        return item


@blp.route("/user")
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
    def post(self, user_data):
        service = UserService(db.session)
        return service.add(user_data, 1)


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserLoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        abort(401, message="Invalid credentials.")
