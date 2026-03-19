from fastapi import FastAPI, Header, HTTPException
from .settings import settings

app = FastAPI(title=settings.app_name)


@app.get("/")
def home():
    return {"message": "Day 5 API Running"}


@app.get("/config")
def config():
    return {"app_name": settings.app_name, "debug": settings.debug}


@app.get("/secure-data")
def secure_data(x_api_key: str = Header(None)):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid key")
    return {"data": "secure access granted"}
