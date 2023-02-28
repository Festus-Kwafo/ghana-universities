from sqlmodel import SQLModel, Field
from typing import Optional


class Universities(SQLModel, table=True):
    __tablename__ = 'universities_data'
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    nickname: Optional[str]
    founded: Optional[str]
    ranking: Optional[str]
    location: Optional[str]
    logo: Optional[str]
    icon: Optional[str]
    website: Optional[str]
    type: Optional[str]
    uniRankId: Optional[str]
    profit: bool
