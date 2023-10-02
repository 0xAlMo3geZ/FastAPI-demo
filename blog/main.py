from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from .database import engine, session_local

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        title=request.title, content=request.content, published=request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    return blog.first()


@app.delete('/blog/{id}')
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        return {'detail': 'Blog not found'}
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'Blog deleted'}


@app.put('/blog/{id}')
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        return {'detail': 'Blog not found'}
    blog.update({'title': request.title, 'content': request.content,
                'published': request.published})
    db.commit()
    return {'detail': 'Blog updated'}
