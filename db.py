from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings


database_url = settings.database_url
engine = create_engine(database_url)


Session = sessionmaker(bind=engine)
Base = declarative_base()
def connect_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()