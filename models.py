from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


URI = 'mysql+pymysql://roman:secret@127.0.0.1:3306/portal'

engine = create_engine(URI)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    name = Column(String(50))
    nickname = Column(String(50))

