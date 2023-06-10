from pydantic import BaseModel


class FishBase(BaseModel):
    species: str
    length = float
    weight = float
    is_released = bool


class FishCreate(FishBase):
    pass


class Fish(FishBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    fish: list[Fish] = []

    class Config:
        orm_mode = True
