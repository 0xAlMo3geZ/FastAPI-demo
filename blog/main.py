from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from .database import engine, session_local
from .hashing import Hash

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


@app.get('/blog', status_code=status.HTTP_200_OK, response_model=list[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='No blogs found')
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    return blog.first()


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'Blog deleted'}


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.update({'title': request.title, 'content': request.content,
                'published': request.published})
    db.commit()
    return {'detail': 'Blog updated'}


@app.post('/user', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash(request.password), is_active=request.is_active)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
