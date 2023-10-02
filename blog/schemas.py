from typing import Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]


class ShowBlog(Blog):
    pass

    class Config:
        orm_mode = True
