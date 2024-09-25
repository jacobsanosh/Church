from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
sql_database_url=os.getenv("MYSQL_URL")
# print("sql url is",sql_database_url)
engine=create_engine(f"mysql+pymysql://{sql_database_url}")
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()