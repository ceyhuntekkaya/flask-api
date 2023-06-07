from sqlalchemy.orm import Session
from project.repository.base_repository import BaseRepository


class SignRepository(BaseRepository):
    entity: object = NotImplementedError
    db: Session = NotImplementedError

    def __init__(self, session: Session, entity: object):
        super().__init__(session, entity)
