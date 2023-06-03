from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required 

from db import db
from models.person.user import UserModel
from schemas.person.user import UserSchema


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

    @jwt_required(fresh=True)
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, item_data):
        item = UserModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A user with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the user.")

        return item
    
