from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.detection.detection import DetectionModel
from schemas.detection.detection import DetectionSchema


blp = Blueprint("Detections", "detections", description="Operations on detection")


@blp.route("/detection/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, DetectionSchema)
    def get(self, item_id):
        item = DetectionModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = DetectionModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Detection deleted"}, 200

     
    @blp.arguments(DetectionSchema)
    @blp.response(201, DetectionSchema)
    def put(self, item_data, item_id):
        item = DetectionModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = DetectionModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/detection")
class Plain(MethodView):
    @blp.response(200, DetectionSchema(many=True))
    def get(self):
        return DetectionModel.query.all()

    @blp.arguments(DetectionSchema)
    @blp.response(201, DetectionSchema)
    def post(self, item_data):
        item = DetectionModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A detection with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the detection.")

        return item
    
