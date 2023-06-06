from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.communication.notification_to import NotificationToListModel
from project.schemas.communication.notification_to import NotificationToListSchema

blp = Blueprint("NotificationToList", "notification_to_list", description="Operations on notification to list")


@blp.route("/notification_to/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, NotificationToListSchema)
    def get(self, item_id):
        item = NotificationToListModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = NotificationToListModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"notification": "notification deleted"}, 200

    @blp.arguments(NotificationToListSchema)
    @blp.response(201, NotificationToListSchema)
    def put(self, item_data, item_id):
        item = NotificationToListModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = NotificationToListModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/notification_to")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, NotificationToListSchema(many=True))
    def get(self):
        return NotificationToListModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(NotificationToListSchema)
    @blp.response(201, NotificationToListSchema)
    def post(self, item_data):
        item = NotificationToListModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                notification="A notification to list with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, notification="An error occurred creating the notification to list.")

        return item
