from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.report.detection_report import DetectionReportModel
from project.schemas.report.detection_report import DetectionReportSchema

blp = Blueprint("DetectionReports", "detection_reports", description="Operations on detection_report")


@blp.route("/detection_report/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, DetectionReportSchema)
    def get(self, item_id):
        item = DetectionReportModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = DetectionReportModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Detection report deleted"}, 200

    @blp.arguments(DetectionReportSchema)
    @blp.response(201, DetectionReportSchema)
    def put(self, item_data, item_id):
        item = DetectionReportModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = DetectionReportModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/detection_report")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, DetectionReportSchema(many=True))
    def get(self):
        return DetectionReportModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(DetectionReportSchema)
    @blp.response(201, DetectionReportSchema)
    def post(self, item_data):
        item = DetectionReportModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A detection report with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the detection report.")

        return item
