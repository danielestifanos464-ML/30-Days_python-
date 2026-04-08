from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = "postgresql+psycopg2://postgres:meseret@localhost:5432/pp"
engine = create_engine(db_url)

session = sessionmaker(autoflush=False, autocommit = False , bind = engine)