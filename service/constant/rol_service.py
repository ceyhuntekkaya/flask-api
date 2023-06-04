from models.constant.role import RoleModel
from db import db



class RolService():
    def create_role(item_data, item_id):
        item = RoleModel(**item_data)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = RoleModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()
        return item