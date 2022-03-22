from enum import unique
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db

Base = declarative_base()
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Result(Base):
    __tablename__ = "result"

    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(UUID(as_uuid=True), unique=True)
    result = db.Column(db.String)
    server_played = db.Column(db.String)
    player_played = db.Column(db.String)
