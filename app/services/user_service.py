"""creating user service"""
from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_respository import (
    create_user,
    delete_user,
    get_user_by_email,
    get_user_by_id,
    get_user
)
from app.core.security import hash_password

def find_user_by_email(
        db: Session,
        email: str,
) -> User | None:

    return get_user_by_email(
        db,
        email
    )
def find_user_by_id(
        db: Session,
        id: int,
) -> User | None:

    return get_user_by_id(
        db,
        id
    )

def list_users(
        db: Session
) -> list[User]:

    return get_user(db)

def register_user(
        db: Session,
        email: str,
        full_name: str,
        password: str
) -> User:

   

    existing_user = get_user_by_email(
        email,
        db
    )

    if existing_user:
        raise ValueError(
            "A User with this Email already Exist"
        )
    hashed_password = hash_password(password)
    
    return create_user(
        db,
        email,
        full_name,
        hashed_password,
    )

def remove_user(
        db: Session,
        user_id: int,
) -> bool:

    user = get_user_by_id(
        db,
        user_id,
    )

    if not user:
        return False

    delete_user(
        db,
        True
    )

    return True