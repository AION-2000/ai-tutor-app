from sqlalchemy.orm import Session
from typing import Optional, Dict, Any

# Corrected imports for your project structure
from ..models.user import User
from ..utils.security import get_password_hash

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """
    Retrieves a user from the database by their email address.
    """
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """
    Retrieves a user from the database by their username.
    """
    return db.query(User).filter(User.username == username).first()

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    """
    Retrieves a user from the database by their unique ID.
    """
    return db.query(User).filter(User.id == user_id).first()

# FIXED: Removed async from function definition
def create_user(db: Session, user: dict) -> User:
    """
    Creates a new user in the database.
    """
    print(f"Crud: Starting user creation for {user['username']}.")

    # Hash the password before storing it for security
    hashed_password = get_password_hash(user["password"])

    # Create a new User model instance with the provided data
    db_user = User(
        email=user["email"],
        username=user["username"],
        hashed_password=hashed_password
    )

    # Use a transaction to ensure atomicity
    try:
        db.add(db_user)
        db.flush()  # Send to DB without committing
        db.commit()  # Commit the transaction
        print(f"Crud: User {user['username']} created successfully.")
    except Exception as e:
        # If anything goes wrong, roll back the entire transaction
        db.rollback()
        print(f"Crud: Error during user creation: {e}. Rolled back.")
        raise e

    # Refresh the instance to get the database-generated ID
    db.refresh(db_user)

    return db_user