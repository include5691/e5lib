from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    dep_id: int
    dep_name: str