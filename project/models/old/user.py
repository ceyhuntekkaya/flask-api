from setting.db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String(255), nullable=False)
