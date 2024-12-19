from pydantic import BaseModel, model_validator
from au_b24 import get_department

class User(BaseModel):
    id: int
    name: str
    dep_id: int
    dep_name: str

    @model_validator(mode="before")
    @classmethod
    def validate_user(cls, data: dict) -> dict:
        data["id"] = data.get("id") or data["ID"]
        data["name"] = data.get("name") or str(data.get("LAST_NAME")).strip() + " " + str(data.get("NAME")).strip()
        data["dep_id"] = data.get("dep_id") or data["UF_DEPARTMENT"][0]
        data["dep_name"] = data.get("dep_name") or get_department(data["dep_id"])["NAME"]
        return data