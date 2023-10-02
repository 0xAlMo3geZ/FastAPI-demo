from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

fake_comments_db = [{'name': 'comment1'}, {
    'name': 'comment2'}, {'name': 'comment3'}]


@app.get("/")
def index():
    return {'data': {'name': 'Blog Page'}}


@app.get('/blog/{id}')
def blog(id: int):
    return {'data': {'name': 'Blog Page', 'id': id}}


@app.get('/blog/{id}/comments')
async def list_comments(skip: int = 0, limit: int = 10):
    return fake_comments_db[skip: skip + limit]


@app.get("/{path:path}")
async def redirect_to_root(path: str):
    return RedirectResponse(url="/")
