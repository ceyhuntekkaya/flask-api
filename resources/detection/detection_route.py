from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.detection.detection_route import DetectionRouteModel
from schemas.detection.detection_route import DetectionRouteSchema


blp = Blueprint("DetectionRoutes", "detection_routes", description="Operations on detection route")


@blp.route("/detection_route/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, DetectionRouteSchema)
    def get(self, item_id):
        item = DetectionRouteModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = DetectionRouteModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Detection route deleted"}, 200

     
    @blp.arguments(DetectionRouteSchema)
    @blp.response(201, DetectionRouteSchema)
    def put(self, item_data, item_id):
        item = DetectionRouteModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = DetectionRouteModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/detection_route")
class Plain(MethodView):
    @blp.response(200, DetectionRouteSchema(many=True))
    def get(self):
        return DetectionRouteModel.query.all()

    @blp.arguments(DetectionRouteSchema)
    @blp.response(201, DetectionRouteSchema)
    def post(self, item_data):
        item = DetectionRouteModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A detection route with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the detection route.")

        return item
    
