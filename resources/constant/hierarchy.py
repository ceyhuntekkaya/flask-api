from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.constant.hierarchy import HierarchyModel
from schemas.constant.hierarchy import HierarchySchema


blp = Blueprint("Hierarchies", "hierarchies", description="Operations on hierarchies")


@blp.route("/hierarchy/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, HierarchySchema)
    def get(self, item_id):
        item = HierarchyModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = HierarchyModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Hierarchy deleted"}, 200

     
    @blp.arguments(HierarchySchema)
    @blp.response(201, HierarchySchema)
    def put(self, item_data, item_id):
        item = HierarchyModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = HierarchyModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/hierarchy")
class Plain(MethodView):
    @blp.response(200, HierarchySchema(many=True))
    def get(self):
        return HierarchyModel.query.all()

    @blp.arguments(HierarchySchema)
    @blp.response(201, HierarchySchema)
    def post(self, item_data):
        item = HierarchyModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A hierarchy with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the hierarchy.")

        return item
    
