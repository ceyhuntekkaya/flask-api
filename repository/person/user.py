from sqlalchemy.orm import Session
from models.person.user import UserModel
from repository.base_repository import BaseRepository

class UserRepository(BaseRepository):

    entity:object = NotImplementedError
    db:Session = NotImplementedError
    
    def __init__(self, session:Session, entity:object): 
        super().__init__(session, entity)