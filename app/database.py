from datetime import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname/<database_name>'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#there is no need of this because using sqlalchemy for database connectivity
# kept for documentation purposes only
#incase we need it (if not using sqlalchemy)
while True:        
    try:
        conn = psycopg2.connect(host='localhost',database='API-Development',user='postgres',password='royalstars', cursor_factory=RealDictCursor)
        cursor = conn.cursor();
        print("Database Connection was Successful")
        break;

    except Exception as error:
        print("connection to database failed")
        print("Error: ", error)
        time.sleep(2)