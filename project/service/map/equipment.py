from sqlalchemy.orm import Session

from project.models.map.equipment import EquipmentModel
from project.repository.map.equipment import EquipmentRepository
import project.service.converters as Converter
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from datetime import datetime


class EquipmentService:
    session: Session = NotImplementedError

    def __init__(self, session: Session):
        self.repo = EquipmentRepository(session, EquipmentModel)

    def add(self, item_data, created_by):
        if self.repo.get_by_name(item_data["name"]):
            return UnexpectedEntityException(
                '{} with name {} was found.'.format(
                    "Item",
                    item_data["name"]
                )
            )

        new_item = EquipmentModel(**item_data)
        item = self.repo.add(new_item, created_by)
        item_created = self.repo.get_by_id(item.id)
        return Converter.convert_object(item_created)

    def getById(self, item_id):
        try:
            item = self.repo.get_by_id(item_id)
            return item
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
            item.name = item_data["name"]
            item.description = item_data["description"]
            item.equipment_type = item_data["equipment_type"]
            item.unit_id = item_data["unit_id"]
            item.lat = item_data["lat"]
            item.lon = item_data["lon"]
            item.standardIdentityFirstDigit = item_data["standardIdentityFirstDigit"]
            item.standardIdentitySecondDigit = item_data["standardIdentitySecondDigit"]
            item.symbolSet = item_data["symbolSet"]
            item.entity = item_data["entity"]
            item.entityType = item_data["entityType"]
            item.sectorIModifier = item_data["sectorIModifier"]
            item.sectorIIModifier = item_data["sectorIIModifier"]
            item.hqTaskforceDummy = item_data["hqTaskforceDummy"]
            item.amplifier = item_data["amplifier"]
            item.symbolCode = item_data["symbolCode"]
            item.src = item_data["src"]
            item.updated_at = datetime.now()

            self.repo.update(item, updated_by)
            return self.repo.get_by_id(item.id)
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
            item.deleted_by = deleted_by
            item.deleted_at = datetime.now()
            item.status = 0
            self.repo.delete(item, deleted_by)
            return self.repo.get_by_id(item.id)
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
