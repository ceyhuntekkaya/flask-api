from sqlalchemy.orm import Session
from project.repository.base_repository import BaseRepository


class SensorRepository(BaseRepository):
    entity: object = NotImplementedError
    db: Session = NotImplementedError

    def __init__(self, session: Session, entity: object):
        super().__init__(session, entity)

    def get_by_sensor_name(self, sensor_name):
        return self.session.query(self.entity).filter(self.entity.sensor_name == sensor_name).all()

    def get_by_unit(self, unit_id):
        try:
            return self.session.query(self.entity).filter(self.entity.unit_id == unit_id).all()
        except Exception as e:
            print(e)




