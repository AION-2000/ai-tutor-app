from pydantic import BaseModel

class UserBase(BaseModel):
    """
    Base model for a user, containing common attributes.
    """
    email: str
    username: str

class UserCreate(UserBase):
    """
    Schema for creating a user. Inherits from UserBase and adds the password.
    """
    password: str

class User(UserBase):
    """
    Schema for a user returned from the API.
    Inherits from UserBase and adds the ID.
    """
    id: int