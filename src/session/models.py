from sqlmodel import SQLModel, Field
from typing import Optional


class Universities(SQLModel, table=True):
    __tablename__ = 'universities_data'
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    acronym: Optional[str]
    website: Optional[str]
    founded: Optional[str]
    description: Optional[str]
    motto: Optional[str]
    ranking: Optional[str]
    colors: Optional[str]
    address: Optional[str]
    logo: Optional[str]
    controlType: Optional[str]
    entityType: Optional[str]
    uniRankId: Optional[str]
    tel: Optional[str]
    fax: Optional[str]
