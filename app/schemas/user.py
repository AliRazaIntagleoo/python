from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    age: int

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str