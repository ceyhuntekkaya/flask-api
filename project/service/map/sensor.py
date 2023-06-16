from sqlalchemy.orm import Session
from project.models.map.sensor import SensorModel
from project.repository.map.sensor import SensorRepository
import project.service.converters as Converter
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from datetime import datetime


class SensorService:
    session: Session = NotImplementedError

    def __init__(self, session: Session):
        self.repo = SensorRepository(session, SensorModel)

    def add(self, item_data, created_by):
        if self.repo.get_by_name(item_data["name"]):
            return UnexpectedEntityException(
                '{} with name {} was found.'.format(
                    "Item",
                    item_data["name"]
                )
            )

        new_item = SensorModel(**item_data)
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
            item.source = item_data["source"]
            item.description = item_data["description"]
            item.hierarchy_id = item_data["hierarchy_id"]
            item.name = item_data["name"]
            item.sensor_weight = item_data["sensor_weight"]
            item.unit_id = item_data["unit_id"]
            item.sensor_type = item_data["sensor_type"]
            item.evaluation_number = item_data["evaluation_number"]
            item.rpm = item_data["rpm"]
            item.detection_range = item_data["detection_range"]
            item.is_fusible = bool(item_data["is_fusible"])
            item.cake_slice = bool(item_data["cake_slice"])
            item.line_of_sight_angle = item_data["line_of_sight_angle"]
            item.line_of_sight_distance = item_data["line_of_sight_distance"]
            item.near_circle = bool(item_data["near_circle"])
            item.circle_radius = item_data["circle_radius"]
            item.circle_time_interval = item_data["circle_time_interval"]
            item.is_meteorology_includes = item_data["is_meteorology_includes"]
            item.latitude = item_data["latitude"]
            item.longitude = item_data["longitude"]
            item.desired_columns = item_data["desired_columns"]
            item.models = item_data["models"]
            item.filters = item_data["filters"]
            item.training_config = item_data["training_config"]
            item.image = item_data["image"],
            item.is_approved = bool(item_data["is_approved"])
            item.aselsan_unit_id = bool(item_data["aselsan_unit_id"])
            item.nvr = item_data["nvr"]
            item.updated_by = item_data["updated_by"]
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
