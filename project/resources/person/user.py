from flask.views import MethodView
from flask_smorest import Blueprint, abort

from project.repository.person.user import UserRepository

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


@blp.route("/user/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, item_id):
        item = UserModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
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
    @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    # @jwt_required(fresh=True)


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
            name=user_data["name"],
            surname=user_data["surname"],
            role_id=user_data["role_id"],
            hierarchy_id=user_data["hierarchy_id"],
            command_id=user_data["command_id"],
            command_collar_mark_id=user_data["command_collar_mark_id"],
            command_collar_mark_rank_id=user_data["command_collar_mark_rank_id"]
        )

        repo = UserRepository(db.session, UserModel)

        item = repo.add(user, 1)
        print("api: ", item.id)
        # if UserModel.query.filter(UserModel.username == user_data["username"]).first():
        #     abort(409, message="A user with that username already exists.")

        # user = UserModel(
        #     username=user_data["username"],
        #     password=pbkdf2_sha256.hash(user_data["password"]),
        # )
        # db.session.add(user)
        # db.session.commit()
        return dict(item)
        # return make_response(jsonify(item), 200)
        # return {"message": "User created successfully.", "item": jsonify(item)}, 201


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
