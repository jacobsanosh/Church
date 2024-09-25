from sqlalchemy import Column,String,Integer
from db.database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(25),unique=True)
    