from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from setting.db import db
from project.models.communication.message_to import MessageToListModel
from project.schemas.communication.message_to import MessageToListSchema

blp = Blueprint("MessageToList", "message_to_list", description="Operations on message to list")


@blp.route("/message_to/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, MessageToListSchema)
    def get(self, item_id):
        item = MessageToListModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = MessageToListModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Message deleted"}, 200

    @blp.arguments(MessageToListSchema)
    @blp.response(201, MessageToListSchema)
    def put(self, item_data, item_id):
        item = MessageToListModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = MessageToListModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/message_to")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, MessageToListSchema(many=True))
    def get(self):
        return MessageToListModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(MessageToListSchema)
    @blp.response(201, MessageToListSchema)
    def post(self, item_data):
        item = MessageToListModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A message to list with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the message to list.")

        return item
