from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(levelname)s:  %(message)s')
logger = logging.getLogger(__name__)

#settings connection
SERVER = os.popen('hostname -i').read().strip()
DATABASE = 'master'
USERNAME = 'sa'
PASSWORD = 'YourPassword01-'

logger.info(f"Connection to the DB Server IP: {SERVER}")
SQLALCHEMY_DATABASE_URL = f'mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
