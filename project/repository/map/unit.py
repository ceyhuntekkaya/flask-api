from sqlalchemy.orm import Session
from project.repository.base_repository import BaseRepository


class UnitRepository(BaseRepository):
    entity: object = NotImplementedError
    db: Session = NotImplementedError

    def __init__(self, session: Session, entity: object):
        super().__init__(session, entity)

    def get_parents_list(self, item_id):
        beginning_getter = self.session.query(self.entity). \
            filter(self.entity.id == item_id).cte(name='parent_for', recursive=True)
        with_recursive = beginning_getter.union_all(
            self.session.query(self.entity).filter(self.entity.id == beginning_getter.c.base_unit_id)
        )
        return self.session.query(with_recursive).all()

    def get_children_list(self, item_id):
        beginning_getter = self.session.query(self.entity). \
            filter(self.entity.id == item_id).cte(name='children_for', recursive=True)
        with_recursive = beginning_getter.union_all(
            self.session.query(self.entity).filter(self.entity.base_unit_id == beginning_getter.c.id)
        )
        return self.session.query(with_recursive).all()
