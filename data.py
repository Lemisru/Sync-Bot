from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from typing import List, Union
#from config import DB_FILE

Base = declarative_base()

from vk_bot.models.professions_base import ProfessionsHandler, Professions_Table
from vk_bot.models.users_base import UsersHandler, Users_Table
    
class DatabaseHandler():
    def __init__(self, db_path):
        self.engine = create_engine('sqlite:///' + db_path)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.users = UsersHandler(self.session)
        self.professions = ProfessionsHandler(self.session)

    def get_data(self, Table: object) -> list:
        return self.session.query(Table).all()

database = DatabaseHandler("data.db")

if __name__ == '__main__':
    ...
    #database.update_user('480980237', name="Лемис")
    #database.professions.add_profession('Минометчик')
