from sqlalchemy.orm import Session
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException


class BaseRepository:
    entity: object = NotImplementedError
    session: Session = NotImplementedError

    def __init__(self, session: Session, entity: object):
        self.session = session
        self.entity = entity

    def get_all(self):
        return self.session.query(self.entity)

    def get_by_id(self, id: int):
        result = self.session.query(self.entity).filter(self.entity.id == id).one()
        if not result:
            raise EntityNotFoundException(
                '{} with id {} was not found.'.format(
                    "Item",
                    id
                )
            )
        return result

    def find_by_id(self, id: int):
        result = self.session.query(self.entity).filter(self.entity.id == id).first()
        if not result:
            raise EntityNotFoundException(
                '{} with id {} was not found.'.format(
                    "Item",
                    id
                )
            )
        return result

    def get_actives(self):
        return self.session.query(self.entity).filter(self.entity.status == 1)

    def add(self, data, created_by: int = None):
        data.created_by = created_by
        if not isinstance(data, self.entity):
            raise UnexpectedEntityException(
                '{} is not a {}'.format(
                    data.__class__.__name__,
                    self.entity.__name__
                )
            )
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        print(data.id)
        return data

    def update(self, entity, updated_by: int = None):
        entity.updated_by = updated_by
        print("____________________________________")
        self.session.add(entity)
        self.session.commit()

    def delete(self, entity, deleted_by: int = None):
        print(entity.deleted_by)
        self.session.add(entity)
        self.session.commit()

    def permanent_delete(self, entity):
        self.session.delete(entity)
        self.session.commit()

    def get_by_name(self, name: str):
        result = self.session.query(self.entity).filter(self.entity.name == name)
        if not result:
            raise EntityNotFoundException(
                '{} with id {} was not found.'.format(
                    "Item",
                    id
                )
            )
        return result


"""



    def get_by_account_id(self, account_id:int):
        return self.session.query(self.entity).filter(self.entity.account_id==account_id)

    def get_actives_by_account_id(self, account_id:int):
        return self.session.query(self.entity).filter\
        (self.entity.is_active==True, self.entity.account_id==account_id)

    def get_by_create_datetime_range(self, from_datetime:datetime, to_datetime:datetime):
        data = self.session.query(self.entity).filter\
        (self.entity.created_datetime >= from_datetime, \
        self.entity.created_datetime <= to_datetime)
        return data

   

"""
