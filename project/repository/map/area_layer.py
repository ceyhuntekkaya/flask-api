from sqlalchemy.orm import Session
from project.repository.base_repository import BaseRepository


class AreaLayerRepository(BaseRepository):
    entity: object = NotImplementedError
    db: Session = NotImplementedError

    def __init__(self, session: Session, entity: object):
        super().__init__(session, entity)

    def get_by_area(self, area_id):
        return self.session.query(self.entity).filter(self.entity.area_id == area_id).all()

    def delete_by_area(self, area_id):
        self.session.query(self.entity).filter(self.entity.area_id == area_id).delete()
        self.session.commit()

    def get_by_layer(self, layer_id):
        return self.session.query(self.entity).filter(self.entity.layer_id == layer_id).all()