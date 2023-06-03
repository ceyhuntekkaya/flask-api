from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.constant.preference import PreferenceModel
from schemas.constant.preference import PreferenceSchema


blp = Blueprint("Preferences", "preferences", description="Operations on preferences")


@blp.route("/preference/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, PreferenceSchema)
    def get(self, item_id):
        item = PreferenceModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = PreferenceModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Preference deleted"}, 200

     
    @blp.arguments(PreferenceSchema)
    @blp.response(201, PreferenceSchema)
    def put(self, item_data, item_id):
        item = PreferenceModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = PreferenceModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/preference")
class Plain(MethodView):
    @blp.response(200, PreferenceSchema(many=True))
    def get(self):
        return PreferenceModel.query.all()

    @blp.arguments(PreferenceSchema)
    @blp.response(201, PreferenceSchema)
    def post(self, item_data):
        item = PreferenceModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A preference with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the preference.")

        return item
    
