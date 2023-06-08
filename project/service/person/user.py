from sqlalchemy.orm import Session
from project.models.person.user import UserModel
from project.repository.person.user import UserRepository
from passlib.hash import pbkdf2_sha256
import project.service.converters as Converter
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException


class UserService:
    session: Session = NotImplementedError

    def __init__(self, session: Session):
        super().__init__(session, UserModel)
        self.repo = UserRepository(session, UserModel)

    def add(self, item_data, created_by):
        if self.repo.get_by_username(item_data["username"]):
            return UnexpectedEntityException(
                '{} with username {} was found.'.format(
                    self.entity.__name__,
                    item_data["username"]
                )
            )
            # return "A user with that username already exists."
        new_item = UserModel(**item_data, password=pbkdf2_sha256.hash(item_data["password"]))
        """
        new_item = UserModel(
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
        """
        item = self.repo.add(new_item, created_by)
        item_created = self.repo.get_by_id(item.id)
        return Converter.convert_user_to_data(item_created)

    def getById(self, item_id):
        try:
            return self.repo.get_by_id(item_id)
        except Exception as e:
            return EntityNotFoundException(
                '{} with username {} was found.'.format(
                    self.entity.__name__,
                    item_id
                )
            )

    def getByName(self, name):
        item = self.repo.get_by_name(name)
        return item

    def update(self, item_data, item_id, updated_by):
        item = self.repo.get_by_id(item_id)
        if item:
            item.username = item_data["username"],
            item.password = pbkdf2_sha256.hash(item_data["password"]),
            item.name = item_data["name"],
            item.surname = item_data["surname"],
            item.role_id = item_data["role_id"],
            item.hierarchy_id = item_data["hierarchy_id"],
            item.command_id = item_data["command_id"],
            item.command_collar_mark_id = item_data["command_collar_mark_id"],
            item.command_collar_mark_rank_id = item_data["command_collar_mark_rank_id"],
            item.update_by = updated_by
            item_updated = self.repo.update(item, updated_by)
            Converter.convert_user_to_data(item_updated)
            return str(item_updated.id)
        else:
            return EntityNotFoundException(
                '{} with item {} was found.'.format(
                    self.entity.__name__,
                    item_id
                )
            )

    def delete(self, item_id, deleted_by):
        item = self.repo.get_by_id(item_id)
        if item:
            item.update_by = deleted_by
            item_deleted = self.repo.delete(item, deleted_by)
            return Converter.convert_user_to_data(item_deleted)
        else:
            return EntityNotFoundException(
                '{} with item {} was found.'.format(
                    self.entity.__name__,
                    item_id
                )
            )

    def permanent_delete(self, item_id):
        item = self.repo.get_by_id(item_id)
        item_permanent_delete = self.repo.permanent_delete(item)
        return str(item_permanent_delete.id)

    def getAll(self):
        item_list = self.repo.get_all()
        return item_list

    def getActive(self):
        item_actives = self.repo.get_actives()
        return item_actives

    def getByUsername(self, username, password):
        try:
            item = self.repo.get_by_username(username).first()
            if item and pbkdf2_sha256.verify(password, item.password):
                return item
        except Exception as e:
            return EntityNotFoundException(
                '{} with username {} was found.'.format(
                    self.entity.__name__,
                    id
                )
            )