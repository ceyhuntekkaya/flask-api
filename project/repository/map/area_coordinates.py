from sqlalchemy.orm import Session
from project.repository.base_repository import BaseRepository


class AreaCoordinateRepository(BaseRepository):
    entity: object = NotImplementedError
    db: Session = NotImplementedError

    def __init__(self, session: Session, entity: object):
        super().__init__(session, entity)

    def get_by_area(self, area_id):
        return self.session.query(self.entity).filter(self.entity.area_id == area_id).all()

    def delete_by_area(self, area_id):
        self.session.query(self.entity).filter(self.entity.area_id == area_id).delete()
        self.session.commit()

