from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.results_model import Base


def engine():
    engine = create_engine(
     "postgresql://postgres:postgres@localhost/postgres"
    )
    Base.metadata.bind = engine
    return engine

Session = sessionmaker(bind=engine())

def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()