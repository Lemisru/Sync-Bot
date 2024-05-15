from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from typing import List, Union

Base = declarative_base()

class Professions_Table(Base):
    __tablename__ = 'professions'

    id = Column(Integer, primary_key=True)
    profession = Column(String, unique=True, nullable=False)

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