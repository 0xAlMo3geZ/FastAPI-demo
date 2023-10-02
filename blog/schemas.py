from typing import Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]


class ShowBlog(Blog):
    pass

    class Config:
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str
    is_active: Optional[bool]
