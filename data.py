from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base

#from config import DB_FILE

Base = declarative_base()

class User_Table(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    rank = Column(Integer, nullable=False)

class DatabaseHandler():
    def __init__(self, db_path):
        self.engine = create_engine('sqlite:///' + db_path)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_all_users(self):
        return self.session.query(User_Table).all()
    
    def get_user_by_id(self, id: int):
        return self.session.get(User_Table, id)
    
    def update_user(self, id: int, name: str=None, rank: int=None):
        user = self.get_user_by_id(id)
        if user is None:
            user = User_Table(id=id, name=name, rank=rank)
            self.session.add(user)
        else:
            if name is not None:
                user.name = name
            if rank is not None:
                user.rank = rank
        self.session.commit()

        return True

database = DatabaseHandler("data.db")

if __name__ == '__main__':
    #database.update_user('480980237', name="Лемис")
    print(database.get_user_by_id(480980237).name)
