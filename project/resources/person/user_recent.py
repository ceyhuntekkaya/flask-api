from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.person.user_recent import UserRecentModel
from project.schemas.person.user_recent import UserRecentSchema

blp = Blueprint("UserRecent", "user_recent", description="Operations on user recent")


@blp.route("/user_recent/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, UserRecentSchema)
    def get(self, item_id):
        item = UserRecentModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = UserRecentModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "User recent deleted"}, 200

    @blp.arguments(UserRecentSchema)
    @blp.response(201, UserRecentSchema)
    def put(self, item_data, item_id):
        item = UserRecentModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = UserRecentModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/user_recent")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, UserRecentSchema(many=True))
    def get(self):
        return UserRecentModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(UserRecentSchema)
    @blp.response(201, UserRecentSchema)
    def post(self, item_data):
        item = UserRecentModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A user recent with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the user recent.")

        return item
