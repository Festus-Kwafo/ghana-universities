import uvicorn
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.session import database
from src.logs import log
from src.utils.scraping import get_all_uni, store_in_db
import strawberry
from strawberry.fastapi import GraphQLRouter
import threading


def my_function():
    get_all_uni()
    store_in_db()


def run_function_every_5_minutes():
    while True:
        # wait for 15 days
        time.sleep(1296000)
        # run the function
        my_function()


# start a new thread to run the function

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)
qraphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(qraphql_app, prefix='/graphql')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["Accept: application/json",
                   "Content-Type: application/json"],
    allow_credentials=["*"])

thread = threading.Thread(target=run_function_every_5_minutes)
thread.start()


@app.on_event('startup')
def init_db():
    try:
        get_all_uni()
        store_in_db()
    except Exception as e:
        log.info(e)
        
        

@app.get('/')
def index():
    log.info("Universities in Ghana API info Started Successfully ", extra={"request_status_code": 200})
    return {'info': "Universities in Ghana API info Started Successfully"}


@app.get('/universities')
def all_uni():
    try:

        return JSONResponse(content=get_all_uni())
    except:
        raise HTTPException(status_code=404, detail="Error scraping the web")


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)
