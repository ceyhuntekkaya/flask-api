from sqlalchemy.orm import Session
from project.models.map.layer import LayerModel
from project.repository.map.layer import LayerRepository
import project.service.converters as Converter
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from datetime import datetime


class LayerService:
    session: Session = NotImplementedError

    def __init__(self, session: Session):
        self.repo = LayerRepository(session, LayerModel)

    def add(self, item_data):
        name_control = self.repo.get_by_name(item_data["name"])
        if len(name_control) > 0:
            return UnexpectedEntityException(
                '{} with name {} was found.'.format(
                    "Item",
                    item_data["name"]
                )
            )
        new_item = LayerModel(**item_data)
        item = self.repo.add(new_item, item_data["created_by"])
        item_created = self.repo.get_by_id(item.id)
        return Converter.convert_object(item_created)

    def getById(self, item_id):
        try:
            return self.repo.get_by_id(item_id)
        except Exception as e:
            return EntityNotFoundException(
                '{} with id {} was found.'.format(
                    "Item",
                    item_id
                )
            )

    def getByName(self, name):
        item = self.repo.get_by_name(name)
        return item

    def update(self, item_data, updated_by):
        item = self.repo.get_by_id(item_data["id"])
        if item:
            item.name = item_data["name"]
            item.description = item_data["description"]
            item.hierarchy_id = item_data["hierarchy_id"]
            item.unit_id = item_data["unit_id"]
            item.status = item_data["status"]
            item.updated_at = datetime.now()
            self.repo.update(item, updated_by)
            return self.repo.get_by_id(item.id)
        else:
            return EntityNotFoundException(
                '{} with item {} was found.'.format(
                    "Item",
                    item.id
                )
            )

    def delete(self, item_id, deleted_by):
        item = self.repo.get_by_id(item_id)
        if item:
            item.deleted_by = deleted_by
            item.deleted_at = datetime.now()
            item.status = 0
            self.repo.delete(item)
            return self.repo.get_by_id(item_id)
        else:
            return EntityNotFoundException(
                '{} with item {} was found.'.format(
                    "Item",
                    item_id
                )
            )

    def permanent_delete(self, item_id):
        item = self.repo.get_by_id(item_id)
        if item:
            self.repo.permanent_delete(item)
            return str(item_id)
        else:
            return EntityNotFoundException(
                '{} with item {} was found.'.format(
                    "Item",
                    item_id
                )
            )

    def getAll(self):
        item_list = self.repo.get_all()
        return item_list

    def getActive(self):
        item_actives = self.repo.get_actives()
        return item_actives

    def getLayerTree(self, item_id):
        item = self.getById(item_id)
        return {"layer": item}
