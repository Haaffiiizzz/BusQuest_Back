from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

databasePassword = os.getenv("DATABASE_PASSWORD")

databaseURL = f"postgresql+psycopg2://postgres:{databasePassword}@localhost/busquest"
engine = create_engine(databaseURL)

Session = sessionmaker(bind=engine)
