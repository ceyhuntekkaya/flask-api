from sqlalchemy.orm import Session

from project.models.map.equipment import EquipmentModel
from project.models.map.layer import LayerModel
from project.models.map.sensor import SensorModel
from project.models.map.unit import UnitModel
from project.models.map.unit_layer import UnitLayerModel
from project.repository.map.equipment import EquipmentRepository
from project.repository.map.layer import LayerRepository
from project.repository.map.sensor import SensorRepository
from project.repository.map.unit import UnitRepository
import project.service.converters as Converter
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from datetime import datetime

from project.repository.map.unit_layer import UnitLayerRepository


class UnitService:
    session: Session = NotImplementedError

    def __init__(self, session: Session):
        self.repo = UnitRepository(session, UnitModel)
        self.repoSensor = SensorRepository(session, SensorModel)
        self.repoUnitLayer = UnitLayerRepository(session, UnitLayerModel)
        self.repoLayer = LayerRepository(session, LayerModel)
        self.repoEquipment = EquipmentRepository(session, EquipmentModel)

    def add(self, item_data, created_by):
        if self.repo.get_by_name(item_data["name"]):
            return UnexpectedEntityException(
                '{} with name {} was found.'.format(
                    "Item",
                    item_data["name"]
                )
            )

        new_item = UnitModel(**item_data)
        item = self.repo.add(new_item, created_by)
        item_created = self.repo.get_by_id(item.id)
        return Converter.convert_object(item_created)

    def getById(self, item_id):
        try:
            item = self.repo.get_by_id(item_id)
            print(item_id)
            item.sensors = self.repoSensor.get_by_unit(item_id)
            item.equipments = self.repoEquipment.get_by_unit(item_id)
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
            item.base_unit_id = item_data["base_unit_id"]
            item.unit_type = item_data["unit_type"]
            item.unit_command = item_data["unit_command"]
            item.hierarchy_id = item_data["hierarchy_id"]
            item.unit_parent = item_data["unit_parent"]
            item.unit_sub = item_data["unit_sub"]
            item.symbol_code = item_data["symbol_code"]
            item.critical_unit_type = item_data["critical_unit_type"]
            item.lat = item_data["lat"]
            item.lon = item_data["lon"]
            item.status = item_data["status"]

            item.standardIdentityFirstDigit = item_data["standardIdentityFirstDigit"]
            item.standardIdentitySecondDigit = item_data["standardIdentitySecondDigit"]
            item.symbolSet = item_data["symbolSet"]
            item.entity = item_data["entity"]
            item.entityType = item_data["entityType"]
            item.sectorIModifier = item_data["sectorIModifier"]
            item.sectorIIModifier = item_data["sectorIIModifier"]
            item.hqTaskforceDummy = item_data["hqTaskforceDummy"]
            item.amplifier = item_data["amplifier"]

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

    def getRecursive(self):
        result = []
        items = self.repo.get_children_list(1)
        for item in items:
            result.append(Converter.convert_object(self.getById(item.id)))
        return result

    # https://stackoverflow.com/questions/38071683/sqlachemy-recursively-fetch-children-and-ancestors-with-relations

    def getChildren(self, item_id):
        result = []
        items = self.repo.get_children_list(item_id)
        for item in items:
            result.append(Converter.convert_object(self.getById(item.id)))
        return result

    def getLayers(self, item_id):
        result = []
        items = self.repo.get_children_list(item_id)
        for item in items:
            layer_unit_list = self.repoUnitLayer.get_by_unit(item.id)
            for layer_unit in layer_unit_list:
                layer_unit.layer = self.repoLayer.get_by_id(layer_unit.layer_id)
                layer_unit.unit = self.getById(layer_unit.unit_id)
                result.append(layer_unit)
        return result
