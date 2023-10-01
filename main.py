from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def index():
    return {'data': {'name': 'Blog Page'}}


@app.get('/blog/{id}')
def blog(id: int):
    return {'data': {'name': 'Blog Page', 'id': id}}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'name': 'Blog Page', 'id': id, 'comments': ['comment1', 'comment2']}}


@app.get("/{path:path}")
async def redirect_to_root(path: str):
    return RedirectResponse(url="/")
