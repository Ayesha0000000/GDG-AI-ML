from typing import Dict, List
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Day 4 FastAPI Project")


# -------------------------
# Models (Pydantic)
# -------------------------
class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    price: float = Field(gt=0)
    in_stock: bool = True


class ItemOut(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


class DivideRequest(BaseModel):
    a: float
    b: float


class DivideResponse(BaseModel):
    result: float


class ErrorResponse(BaseModel):
    error_type: str
    message: str
    details: list | None = None


# -------------------------
# Fake Database
# -------------------------
items: Dict[int, ItemOut] = {}
next_id = 1


# -------------------------
# Custom Error Handling
# -------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            error_type="validation_error",
            message="Invalid request",
            details=exc.errors(),
        ).dict(),
    )


# -------------------------
# Routes
# -------------------------


# Health check
@app.get("/health")
def health():
    return {"status": "ok"}


# Create item
@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(payload: ItemCreate):
    global next_id
    item = ItemOut(id=next_id, **payload.dict())
    items[next_id] = item
    next_id += 1
    return item


# Get all items
@app.get("/items", response_model=List[ItemOut])
def list_items():
    return list(items.values())


# Get single item
@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


# Delete item
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return None


# Divide API
@app.post("/math/divide", response_model=DivideResponse)
def divide(payload: DivideRequest):
    if payload.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero not allowed")
    return DivideResponse(result=payload.a / payload.b)
