import uvicorn
import time
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from session import database
from logs import log
from utils.scraping import get_all_uni, store_in_db
import strawberry
from strawberry.fastapi import GraphQLRouter
import threading
from sqlmodel import Session
from schema import UniversitySchema
from func.handler import get_uni_by_rank
def my_function():
    get_all_uni()
    store_in_db()


def run_function_every_15_days():
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

thread = threading.Thread(target=run_function_every_15_days)
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

@app.get('/universities/{rank}', response_model=UniversitySchema )
def get_uni_rank(rank: str, db: Session = Depends(database.get_db)):
    return get_uni_by_rank(rank, db)


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)
