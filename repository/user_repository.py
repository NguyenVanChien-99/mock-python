from entity.user import User
from database.data_source import db


class UserRepository:

    @classmethod
    def save(cls, user: User) -> User:
        # save user
        user.id = None
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        return user

    @classmethod
    def update(cls, user: User) -> User:
        db.session.commit()
        db.session.refresh(user)
        return user

    @classmethod
    def find_by_email(cls, email) -> User:
        return db.session.query(User).filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id: int) -> User:
        return db.session.query(User).filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username: str):
        return db.session.query(User).filter_by(username=username).first()
