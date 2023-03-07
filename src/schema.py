from pydantic import BaseModel
from typing import Optional


class UniversitySchema(BaseModel):
    name: str 
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