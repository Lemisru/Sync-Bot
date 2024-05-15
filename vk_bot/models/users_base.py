from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from typing import List, Union

Base = declarative_base()

class Users_Table(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    chat_id = Column(Integer)
    user_id = Column(Integer, nullable=False)

    name = Column(String)
    admin_rank = Column(Integer, default=0, nullable=False)

class UsersHandler():
    def __init__(self, session: Session):
        self.session = session

    def get_chat_user_info(self, chat_id: int, user_id: int) -> Users_Table:
        return self.session.query(Users_Table).filter(Users_Table.chat_id == chat_id, 
                                                      Users_Table.user_id == user_id).first()
    
    def update_user(self, chat_id: int, user_id: int, name: str=None, admin_rank: int=None) -> bool:
        user_table = Users_Table(chat_id=chat_id, user_id=user_id, name=name, admin_rank=admin_rank)
        user = self.get_chat_user_info(chat_id, user_id)

        if user is None:
            self.session.add(user_table)
            self.session.commit()
            return True
        
        if name is not None:
            user.name = name
            
        if admin_rank is not None:
            user.rank = admin_rank

        self.session.commit()

        return True
    
