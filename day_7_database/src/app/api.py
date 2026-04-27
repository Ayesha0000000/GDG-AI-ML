from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, SessionLocal, Base
from . import models, schemas

app = FastAPI()

# Table create karo
Base.metadata.create_all(bind=engine)


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create item
@app.post("/items")
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    new_item = models.Item(name=item.name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


# Get items
@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()
