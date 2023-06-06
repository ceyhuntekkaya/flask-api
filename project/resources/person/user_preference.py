from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.person.user_preference import UserPreferenceModel
from project.schemas.person.user_preference import UserPreferenceSchema

blp = Blueprint("UserPreferences", "user_preferences", description="Operations on user preference")


@blp.route("/user_preference/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, UserPreferenceSchema)
    def get(self, item_id):
        item = UserPreferenceModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = UserPreferenceModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "User preference deleted"}, 200

    @blp.arguments(UserPreferenceSchema)
    @blp.response(201, UserPreferenceSchema)
    def put(self, item_data, item_id):
        item = UserPreferenceModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = UserPreferenceModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/user_preference")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, UserPreferenceSchema(many=True))
    def get(self):
        return UserPreferenceModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(UserPreferenceSchema)
    @blp.response(201, UserPreferenceSchema)
    def post(self, item_data):
        item = UserPreferenceModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A user preference with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the user preference.")

        return item
