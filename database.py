from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
URL_Database = "mysql+mysqlconnector://mydb:neosdb@172.17.0.2:3306/banco"

engine = create_engine(URL_Database)

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()