from sqlalchemy.orm import Session

from project.models.map.unit_layer import UnitLayerModel
from project.repository.map.unit_layer import UnitLayerRepository
import project.service.converters as Converter
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException


class UnitLayerService:
    session: Session = NotImplementedError

    def __init__(self, session: Session):
        self.repo = UnitLayerRepository(session, UnitLayerModel)

    def add(self, item_data, created_by):
        if self.repo.get_by_name(item_data["name"]):
            return UnexpectedEntityException(
                '{} with name {} was found.'.format(
                    "Item",
                    item_data["name"]
                )
            )

        new_item = UnitLayerModel(**item_data )
        item = self.repo.add(new_item, created_by)
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

    def update(self, item_data, item_id, updated_by):
        item = self.repo.get_by_id(item_id)
        if item:
            item.name = item_data["name"],

            item.updated_by = item_data["updated_by"],
            item_updated = self.repo.update(item, updated_by)

            Converter.convert_object(item_updated)
            return str(item_updated.id)
        else:
            return EntityNotFoundException(
                '{} with item {} was found.'.format(
                    "Item",
                    item_id
                )
            )

    def delete(self, item_id, deleted_by):
        item = self.repo.get_by_id(item_id)
        if item:
            item.updated_by = deleted_by
            item_deleted = self.repo.delete(item, deleted_by)
            return Converter.convert_object(item_deleted)
        else:
            return EntityNotFoundException(
                '{} with item {} was found.'.format(
                    "Item",
                    item_id
                )
            )

    def permanent_delete(self, item_id):
        item = self.repo.get_by_id(item_id)
        item_permanent_delete = self.repo.permanent_delete(item)
        return str(item_permanent_delete.id)

    def getAll(self):
        item_list = self.repo.get_all()
        return item_list

    def getActive(self):
        item_actives = self.repo.get_actives()
        return item_actives
