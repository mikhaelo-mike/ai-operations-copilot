"""creating user service"""
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_respository import get_user_by_email

def find_user_by_email(
        db: Session,
        email: str,
) -> User | None:

    return get_user_by_email(
        db,
        email
    )