from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.library.media_source import MediaSourceModel
from project.schemas.library.media_source import MediaSourceSchema

blp = Blueprint("MediaSourses", "media_sourses", description="Operations on media sourse")


@blp.route("/media_sourse/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, MediaSourceSchema)
    def get(self, item_id):
        item = MediaSourceModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = MediaSourceModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "media sourse deleted"}, 200

    @blp.arguments(MediaSourceSchema)
    @blp.response(201, MediaSourceSchema)
    def put(self, item_data, item_id):
        item = MediaSourceModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = MediaSourceModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/media_sourse")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, MediaSourceSchema(many=True))
    def get(self):
        return MediaSourceModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(MediaSourceSchema)
    @blp.response(201, MediaSourceSchema)
    def post(self, item_data):
        item = MediaSourceModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A media sourse with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the media sourse.")

        return item
