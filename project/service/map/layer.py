from sqlalchemy.orm import Session

from project.models.map.area import AreaModel
from project.models.map.area_coordinates import AreaCoordinateModel
from project.models.map.area_layer import AreaLayerModel
from project.models.map.layer import LayerModel
from project.models.map.sensor import SensorModel
from project.models.map.unit import UnitModel
from project.repository.map.area import AreaRepository
from project.repository.map.area_coordinates import AreaCoordinateRepository
from project.repository.map.area_layer import AreaLayerRepository
from project.repository.map.layer import LayerRepository
import project.service.converters as Converter
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from datetime import datetime

from project.repository.map.sensor import SensorRepository
from project.repository.map.unit import UnitRepository


class LayerService:
    session: Session = NotImplementedError

    def __init__(self, session: Session):
        self.repo = LayerRepository(session, LayerModel)
        self.repoSensor = SensorRepository(session, SensorModel)
        self.repoUnit = UnitRepository(session, UnitModel)
        self.repoArea = AreaRepository(session, AreaModel)
        self.repoAreaLayer = AreaLayerRepository(session, AreaLayerModel)
        self.repoAreaCoordinate = AreaCoordinateRepository(session, AreaCoordinateModel)

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
            item = self.repo.get_by_id(item_id)
            item.sensors = self.repoSensor.get_by_unit(item.unit_id)
            item.units = self.repoUnit.get_children_list(item.unit_id)
            return item
        except Exception as e:
            return EntityNotFoundException(
                '{} with id {} was found.'.format(
                    "Item",
                    item_id
                )
            )

    def getByName(self, name):
        item_list = []
        items = self.repo.get_by_name(name)
        for item in items:
            item.sensors = self.repoSensor.get_by_unit(item.unit_id)
            item.units = self.repoUnit.get_children_list(item.unit_id)
            item_list.append(item)
        return item_list

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
        item_list = []
        items = self.repo.get_all()
        for item in items:
            item.sensors = self.repoSensor.get_by_unit(item.unit_id)
            item.units = self.repoUnit.get_children_list(item.unit_id)
            item_list.append(item)
        return item_list

    def getActive(self):
        item_list = []
        items = self.repo.get_actives()
        for item in items:
            item.sensors = self.repoSensor.get_by_unit(item.unit_id)
            item.units = self.repoUnit.get_children_list(item.unit_id)
            item_list.append(item)
        return item_list

    def getLayerTree(self, item_id):
        item = self.getById(item_id)
        areas = []
        units = self.repoUnit.get_children_list(item_id)
        area_layer_list = self.repoAreaLayer.get_by_layer(item_id)
        for area_layer in area_layer_list:
            area_item = {}
            area_id = area_layer.area_id
            area = self.repoArea.get_by_id(area_id)
            area_item["area"] = area
            area_coordinates = self.repoAreaCoordinate.get_by_area(area_id)
            area_item["coordinates"] = area_coordinates
            areas.append(area_item)

        return {"layer": item, "units": units, "areas": areas}
