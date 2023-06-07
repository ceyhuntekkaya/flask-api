from sqlalchemy.orm import Session
from project.repository.base_repository import BaseRepository
from project.models.person.user import UserModel
from project.repository.person.user import UserRepository
from passlib.hash import pbkdf2_sha256
from project.service.converters import UserConverter


class UserService(BaseRepository):
    db: Session = NotImplementedError

    def __init__(self, session: Session):
        super().__init__(session, UserModel)
        self.repo = UserRepository(session, UserModel)

    def add(self, item_data, created_by):
        user = UserModel(
            username=item_data["username"],
            password=pbkdf2_sha256.hash(item_data["password"]),
            name=item_data["name"],
            surname=item_data["surname"],
            role_id=item_data["role_id"],
            hierarchy_id=item_data["hierarchy_id"],
            command_id=item_data["command_id"],
            command_collar_mark_id=item_data["command_collar_mark_id"],
            command_collar_mark_rank_id=item_data["command_collar_mark_rank_id"]
        )
        item = self.repo.add(user, created_by)
        item_created = self.repo.get_by_id(item.id)
        return UserConverter.convert_object_to_data(item_created)

    def getById(self, id):
        item = self.repo.get_by_id(id)
        return item

    def getByName(self, name):
        item = self.repo.get_by_name(name)
        return item

    def update(self, item, updated_by):
        item_updated = self.repo.update(item, updated_by)
        return str(item_updated.id)

    def delete(self, item, deleted_by):
        item_deleted = self.repo.delete(item, deleted_by)
        return str(item_deleted.id)

    def permanent_delete(self, item):
        item_permanent_delete = self.repo.permanent_delete(item)
        return str(item_permanent_delete.id)

    def getAll(self):
        item_list = self.repo.get_all()
        return item_list

    def getActive(self):
        item_actives = self.repo.get_actives()
        return item_actives
