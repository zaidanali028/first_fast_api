# making a virtual env - pip -m ven venv
# activate venvsource - venv/bin/activate
from fastapi import FastAPI,Request
import uvicorn
from database.connection import Settings
from routes import routelist
app=FastAPI()
settings=Settings()

@app.on_event('startup')
async def init_db():
    await settings.init_db()

@app.get('/')
def root(request: Request) -> dict:
    return {
        "msg":"Hello  From FastApi"
    }

app.include_router(routelist.todo_router,prefix='/todo')
 
# python3 ./app/root.py


if __name__=="__main__":
    uvicorn.run('main:app',host="127.0.0.1",port=8000,reload=True)





