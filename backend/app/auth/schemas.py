from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    username: str

class User(UserBase):
    id: int
    username: str
    is_active: bool

    class Config:
        from_attributes = True  

class Token(BaseModel):
    access_token: str
    token_type: str
