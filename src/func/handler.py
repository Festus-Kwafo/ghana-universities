from fastapi import status, Depends
from sqlmodel import Session, select
from session.models import Universities

def get_uni_by_rank(rank: str, db: Session):
    statement =  select(Universities).where(Universities.ranking == rank)
    results = db.exec(statement)
    uni_session = results.one()
    return uni_session

def get_all_uni(db: Session):
    statement = select(Universities)
    results = db.execute(statement)
    uni_session = results.scalars().all()
    return uni_session