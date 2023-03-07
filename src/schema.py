from pydantic import BaseModel
from typing import Union


class UniversitySchema(BaseModel):
    name: Union[str, None] = None 
    acronym: Union[str, None] = None
    website: Union[str, None] = None
    founded: Union[str, None] = None
    description: Union[str, None] = None
    motto: Union[str, None] = None
    ranking: Union[str, None] = None
    colors: Union[str, None] = None
    address: Union[str, None] = None
    logo: Union[str, None] = None
    controlType: Union[str, None] = None
    entityType: Union[str, None] = None
    uniRankId: Union[str, None] = None
    tel: Union[str, None] = None
    fax: Union[str, None] = None