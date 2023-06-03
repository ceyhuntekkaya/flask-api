from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.communication.notification import NotificationModel
from schemas.communication.notification import NotificationSchema


blp = Blueprint("Notifications", "notifications", description="Operations on notifications")


@blp.route("/notification/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, NotificationSchema)
    def get(self, item_id):
        item = NotificationModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = NotificationModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "notification deleted"}, 200

     
    @blp.arguments(NotificationSchema)
    @blp.response(201, NotificationSchema)
    def put(self, item_data, item_id):
        item = NotificationModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = NotificationModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/notification")
class Plain(MethodView):
    @blp.response(200, NotificationSchema(many=True))
    def get(self):
        return NotificationModel.query.all()

    @blp.arguments(NotificationSchema)
    @blp.response(201, NotificationSchema)
    def post(self, item_data):
        item = NotificationModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A notification with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the notification.")

        return item
    