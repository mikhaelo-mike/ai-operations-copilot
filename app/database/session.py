"""Creatin gthe database Engine"""
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session

from app.core.config import get_settings

settings = get_settings()

engine = create_engine(
    settings.database_url
)

sessionlocal = sessionmaker (
    bind = engine,
    autoflash = False,
    autocommit = False
)

def get_db() -> Generator[Session, None, None]:
    db = sessionlocal()

    try:
        yield db
    finally:
        db.close()