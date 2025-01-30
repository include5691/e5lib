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
        data["id"] = data.get("id") or data.get("ID")
        data["name"] = data.get("name") or data.get("LAST_NAME", "").strip() + " " + data.get("NAME", "").strip()
        dep_id = data.get("dep_id")
        if not dep_id:
            dep_ids = data.get("UF_DEPARTMENT")
            if dep_ids and isinstance(dep_ids, list):
                dep_id = dep_ids[0]
        data["dep_id"] = dep_id
        dep_name = data.get("dep_name")
        if not dep_name:
            department = get_department(dep_id)
            if department:
                dep_name = department.get("NAME")
        data["dep_name"] = dep_name
        return data