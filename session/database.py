from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

def get_db():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)