from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from setting.db import db
from project.models.communication.message_template import MessageTemplateModel
from project.schemas.communication.message_template import MessageTemplateSchema

blp = Blueprint("MessageTemplates", "message_templates", description="Operations on message templates")


@blp.route("/message_template/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, MessageTemplateSchema)
    def get(self, item_id):
        item = MessageTemplateModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = MessageTemplateModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Message Template deleted"}, 200

    @blp.arguments(MessageTemplateSchema)
    @blp.response(201, MessageTemplateSchema)
    def put(self, item_data, item_id):
        item = MessageTemplateModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = MessageTemplateModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/message_template")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, MessageTemplateSchema(many=True))
    def get(self):
        return MessageTemplateModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(MessageTemplateSchema)
    @blp.response(201, MessageTemplateSchema)
    def post(self, item_data):
        item = MessageTemplateModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A Message Template with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the message template.")

        return item
