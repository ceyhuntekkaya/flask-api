from datetime import datetime


class BaseModelClass:
    __table__ = None

    def __init__(self, *args, **kwargs):
        pass

    async def as_dict(self):
        return {
            c.name: getattr(self, c.name).isoformat()
            if isinstance(getattr(self, c.name), datetime)
            else getattr(self, c.name)
            for c in self.__table__.columns
        }
