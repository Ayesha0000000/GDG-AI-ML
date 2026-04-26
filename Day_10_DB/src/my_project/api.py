from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .models import Item

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Day 10 API running"}


@app.post("/db/items")
def create_item(db: Session = Depends(get_db)):
    item = Item(name="Test Item", price=100.0, in_stock=True)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.get("/db/items")
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
