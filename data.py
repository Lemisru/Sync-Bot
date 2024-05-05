from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from typing import List, Union
#from config import DB_FILE

Base = declarative_base()

class Users_Table(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rank = Column(Integer, nullable=False)

class Professions_Table(Base):
    __tablename__ = 'professions'

    id = Column(Integer, primary_key=True)
    profession = Column(String, unique=True, nullable=False)
    
class UserHandler():
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, id: int) -> Professions_Table:
        return self.session.get(Users_Table, id)
    
    def update_user(self, id: int, name: str=None, rank: int=None) -> bool:
        user = self.get_user_by_id(id)
        if user is None:
            user = Users_Table(id=id, name=name, rank=rank)
            self.session.add(user)
        else:
            if name is not None:
                user.name = name
            if rank is not None:
                user.rank = rank
        self.session.commit()

        return True
    
class ProfessionsHandler():
    def __init__(self, session: Session):
        self.session = session

    def get_professions(self) -> List[Professions_Table]:
        professions_list = self.session.query(Professions_Table).all()
        return self.session.query(Professions_Table).all()
    
    def _add_profession(self, profession: Union[str, List[str]]) -> bool:
        if self.session.query(Professions_Table).filter_by(profession=profession).first():
            return False

        profession = Professions_Table(profession=profession)
        self.session.add(profession)
        self.session.commit()

        return True
    
    def add_professions(self, professions: Union[str, List[str]]) -> bool:
        if isinstance(professions, list):
            for profession in professions:
                result = self._add_profession(profession)
        else:
            result = self._add_profession(profession)

        return result
    
class DatabaseHandler():
    def __init__(self, db_path):
        self.engine = create_engine('sqlite:///' + db_path)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.users = UserHandler(self.session)
        self.professions = ProfessionsHandler(self.session)

    def get_data(self, Table: object) -> list:
        return self.session.query(Table).all()

database = DatabaseHandler("data.db")

if __name__ == '__main__':
    #database.update_user('480980237', name="Лемис")
    #database.professions.add_profession('Минометчик')

    with open('data/professions.txt', 'r') as f:
        professions = [line.strip() for line in f]

    database.professions.add_professions(professions)

    print(database.professions.get_professions())
