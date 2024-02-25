# making a virtual env - pip -m ven venv
# activate venvsource - venv/bin/activate
from fastapi import FastAPI, Request

from app.database.connection import Settings
from app.routers.routes import ROUTES

app = FastAPI(title="Todo Manager")
settings = Settings()


@app.on_event("startup")
async def init_db():
    await settings.init_db()


@app.get("/")
def index(request: Request) -> dict:
    return {"msg": "Hello  From FastApi"}


for router in ROUTES:
    app.include_router(router, prefix="/api/v1")

# if __name__=="__main__":
#    uvicorn.run('main:app',host="127.0.0.1",port=8000,reload=True)
