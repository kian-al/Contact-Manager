from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("CONTACT_DB_URL", "postgresql://cm_user:pass@localhost:5432/contactdb")

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

def init_db():
    from .models import Contact
    Base.metadata.create_all(bind=engine)
