from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from fastapi.responses import RedirectResponse

app = FastAPI()

fake_comments_db = [{'name': 'comment1'}, {
    'name': 'comment2'}, {'name': 'comment3'}]


@app.get("/")
def index():
    return {'data': {'name': 'Blog Page'}}


class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': request}


@app.get('/blog/{id}')
def blog(id: int):
    return {'data': {'name': 'Blog Page', 'id': id}}


@app.get('/blog/{id}/comments')
async def list_comments(skip: int = 0, limit: int = 10):
    return fake_comments_db[skip: skip + limit]


# @app.get("/{path:path}")
# async def redirect_to_root(path: str):
#     return RedirectResponse(url="/")


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"detail": "Not Found"}
