from sqlalchemy.orm import Session
from project.repository.base_repository import BaseRepository


class EquipmentRepository(BaseRepository):
    entity: object = NotImplementedError
    db: Session = NotImplementedError

    def __init__(self, session: Session, entity: object):
        super().__init__(session, entity)


    def get_by_unit(self, unit_id):
        try:
            return self.session.query(self.entity).filter(self.entity.unit_id == unit_id).all()
        except Exception as e:
            print(e)





