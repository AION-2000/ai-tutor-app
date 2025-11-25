from datetime import timedelta
from typing import Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt

# Corrected imports
from ..models import get_db, User
from ..database import crud
from ..utils.security import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, verify_password

# Create a router instance
router = APIRouter()

# This scheme will extract the token from the Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/token")

# --- Endpoints ---

@router.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """
    Simple health check to verify database connection
    """
    try:
        # Try to execute a simple query
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        print(f"Health check failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed"
        )

@router.post("/register")
async def register(request: Request, user_data: dict, db: Session = Depends(get_db)):
    """
    Registers a new user.
    """
    print("\n--- /register endpoint called ---")
    print(f"Request data: {user_data}")

    # Check if user with this email already exists
    db_user = crud.get_user_by_email(db, email=user_data["email"])
    if db_user:
        print("Error: Email already registered")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Check if username is taken
    db_user = crud.get_user_by_username(db, username=user_data["username"])
    if db_user:
        print("Error: Username already taken")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    # FIXED: Removed await from create_user call
    print("Crud: Calling create_user.")
    crud.create_user(db=db, user=user_data)

    print("\n--- /register endpoint finished ---")
    return {"message": "User registered successfully"}


@router.post("/token")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    """
    Logs in a user and returns an access token.
    """
    print("\n--- /token endpoint called ---")

    # Log the parsed form data from FastAPI's dependency
    print(f"Parsed Form Data: username={form_data.username}, password={form_data.password}")

    user = crud.get_user_by_username(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        print("Error: Incorrect username or password")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    print(f"Success: User {form_data.username} logged in.")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    response_data = {"access_token": access_token, "token_type": "bearer"}

    print(f"--- SENDING RESPONSE ---")
    print(response_data)
    print("--- END RESPONSE ---")

    return response_data