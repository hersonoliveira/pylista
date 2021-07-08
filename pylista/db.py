from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE_URL = ""
engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL,
    echo=True,
    future=True)

SessionLocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()
