from db.models import User
from sqlalchemy.orm import Session
from utils.secrets import password_manager
from utils.jwt import create_access_token
from schema.output import RegisterOutput, LoginOutput
import exceptions

class UsersOpration:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create(self, username: str, password: str) -> RegisterOutput:
        user_password = password_manager.hash(password)
        user = User(username=username, password=user_password)
        self.db_session.add(user)
        self.db_session.commit()
        self.db_session.refresh(user)
        return RegisterOutput(username=user.username, id=user.id)

    def get_by_username(self, username: str) -> User:
        user_data = self.db_session.query(User).filter(User.username == username).first()
        if user_data is None:
            raise exceptions.UserNotFound
        return user_data

    def update_username(self, old_username: str, new_username: str) -> User:
        user = self.db_session.query(User).filter(User.username == old_username).first()
        if user is None:
            raise exceptions.UserNotFound
        user.username = new_username
        self.db_session.commit()
        self.db_session.refresh(user)
        return user

    def user_delete_account(self, username: str, password: str) -> bool:
        user = self.db_session.query(User).filter(User.username == username).first()
        if user is None:
            return False
        if not password_manager.verify(password, user.password):
            return False
        self.db_session.delete(user)
        self.db_session.commit()
        return True

    def check_user_login(self, username: str, password: str) -> LoginOutput:
        user = self.db_session.query(User).filter(User.username == username).first()
        if user is None:
            raise exceptions.UsernameOrPasswordIsIncorrect
        if not password_manager.verify(password, user.password):
            raise exceptions.UsernameOrPasswordIsIncorrect

        access_token = create_access_token(user.username)
        return LoginOutput(access_token=access_token, token_type="bearer")
