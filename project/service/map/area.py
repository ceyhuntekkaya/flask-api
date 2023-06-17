from sqlalchemy.orm import Session
from project.models.map.area import AreaModel
from project.models.map.area_coordinates import AreaCoordinateModel
from project.models.map.area_layer import AreaLayerModel
from project.models.map.layer import LayerModel
from project.repository.map.area import AreaRepository
import project.service.converters as Converter
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from project.repository.map.area_coordinates import AreaCoordinateRepository
from project.repository.map.area_layer import AreaLayerRepository
from project.repository.map.layer import LayerRepository
from project.service.map.area_layer import AreaLayerService
from project.service.map.area_coordinates import AreaCoordinateService
from datetime import datetime


class AreaService:
    session: Session = NotImplementedError

    def __init__(self, session: Session):
        self.session = session
        self.repo = AreaRepository(session, AreaModel)
        self.repoAreaCoordinate = AreaCoordinateRepository(session, AreaCoordinateModel)
        self.repoLayer = LayerRepository(session, LayerModel)
        self.repoAreaLayer = AreaLayerRepository(session, AreaLayerModel)

    def add(self, item_data, created_by):
        if self.repo.get_by_name(item_data["area"]["name"]):
            return UnexpectedEntityException(
                '{} with name {} was found.'.format(
                    "Item",
                    item_data["area"]["name"]
                )
            )

        new_item = AreaModel(**item_data["area"])
        item = self.repo.add(new_item, created_by)
        item_id = item.id
        layer_service = AreaLayerService(self.session)
        layer_service.add_all(item_data["layers"], created_by, item_id)
        coordinate_service = AreaCoordinateService(self.session)
        coordinate_service.add_all(item_data["coordinates"], created_by, item_id)
        item_created = self.repo.get_by_id(item.id)
        return Converter.convert_object(item_created)

    def getById(self, item_id):
        try:
            item = self.repo.get_by_id(item_id)
            item.coordinates = self.getCoordinates(item_id)
            item.layers = self.getLayers(item_id)
            return item
        except Exception as e:
            return EntityNotFoundException(
                '{} with id {} was found.'.format(
                    "Item",
                    item_id
                )
            )

    def getByCoordinates(self, item_id):
        try:
            item = self.repo.get_by_id(item_id)
            item.coordinates = self.getCoordinates(item_id)
            return item
        except Exception as e:
            return EntityNotFoundException(
                '{} with id {} was found.'.format(
                    "Item",
                    item_id
                )
            )

    def getCoordinates(self, area_id):
        return self.repoAreaCoordinate.get_by_area(area_id)

    def getLayers(self, area_id):
        layers = []
        area_layers = self.repoAreaLayer.get_by_area(area_id)
        for area_layer in area_layers:
            layer = self.repoLayer.get_by_id(area_layer.layer_id)
            layers.append(layer)
        return layers

    def getByName(self, name):
        item_active_list = []
        item_list = self.repo.get_by_name(name)
        for item in item_list:
            item = self.repo.get_by_id(item.id)
            item.coordinates = self.getCoordinates(item.id)
            item.layers = self.getLayers(item.id)
            item_active_list.append(item)
        return item_active_list

    def update(self, item_data, item_id, updated_by):
        item = self.repo.get_by_id(item_id)
        if item:
            item.name = item_data["area"]["name"]
            item.description = item_data["area"]["description"]
            item.hierarchy_id = item_data["area"]["hierarchy_id"]
            item.area_type = item_data["area"]["area_type"]
            item.area_parent = item_data["area"]["area_parent"]
            item.area_sub = item_data["area"]["area_sub"]
            item.symbol_code = item_data["area"]["symbol_code"]
            item.critical_area_type = item_data["area"]["critical_area_type"]
            item.color = item_data["area"]["color"]
            item.status = item_data["area"]["status"]
            item.updated_by = item_data["area"]["updated_by"]
            item.updated_at = datetime.now()
            self.repo.update(item, updated_by)

            self.repoAreaLayer.delete_by_area(item_id)
            self.repoAreaCoordinate.delete_by_area(item_id)

            layer_service = AreaLayerService(self.session)
            layer_service.add_all(item_data["layers"], updated_by, item_id)
            coordinate_service = AreaCoordinateService(self.session)
            coordinate_service.add_all(item_data["coordinates"], updated_by, item_id)

            return self.getById(item_id)
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
            return self.getById(item_id)
        else:
            return EntityNotFoundException(
                '{} with item {} was found.'.format(
                    "Item",
                    item_id
                )
            )

    def permanent_delete(self, item_id):
        item = self.repo.get_by_id(item_id)
        self.repoAreaLayer.delete_by_area(item_id)
        self.repoAreaCoordinate.delete_by_area(item_id)
        self.repo.permanent_delete(item)
        return str(item_id)

    def getAll(self):
        item_active_list = []
        item_list = self.repo.get_all()
        for item in item_list:
            item = self.repo.get_by_id(item.id)
            item.coordinates = self.getCoordinates(item.id)
            item.layers = self.getLayers(item.id)
            item_active_list.append(item)
        return item_active_list

    def getActive(self):
        item_active_list = []
        item_actives = self.repo.get_actives()
        for item in item_actives:
            item = self.repo.get_by_id(item.id)
            item.coordinates = self.getCoordinates(item.id)
            item.layers = self.getLayers(item.id)
            item_active_list.append(item)
        return item_active_list
