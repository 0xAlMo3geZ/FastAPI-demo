from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'data': {'name': 'Home Page'}}


@app.get("/about")
def about():
    return {'data': {'name': 'About Page'}}
