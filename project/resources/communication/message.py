from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.communication.message import MessageModel
from project.schemas.communication.message import MessageSchema

blp = Blueprint("Messages", "messages", description="Operations on messages")


@blp.route("/message/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, MessageSchema)
    def get(self, item_id):
        item = MessageModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = MessageModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Message deleted"}, 200

    @blp.arguments(MessageSchema)
    @blp.response(201, MessageSchema)
    def put(self, item_data, item_id):
        item = MessageModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = MessageModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/message")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, MessageSchema(many=True))
    def get(self):
        return MessageModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(MessageSchema)
    @blp.response(201, MessageSchema)
    def post(self, item_data):
        item = MessageModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A message with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the message.")

        return item
