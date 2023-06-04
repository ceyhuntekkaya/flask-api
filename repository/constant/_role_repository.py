import abc
from models.constant.role import RoleModel


class AbstractRepository(abc.ABC):
    def add(self, batch: RoleModel):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> RoleModel:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, item):
        self.session.add(item)

    def get(self, reference):
        return self.session.query(RoleModel).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(RoleModel).all()