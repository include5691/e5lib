from typing import Annotated
from fastapi import Form, HTTPException


def get_bitrix_form_entity_id(
    document_id2: Annotated[str, Form(alias="document_id[2]")],
) -> int:
    parts = document_id2.split("_", 1)
    if len(parts) != 2:
        raise HTTPException(status_code=400, detail="Invalid document_id[2] format")
    lead_id = parts[1]
    if not lead_id.isdecimal():
        raise HTTPException(status_code=400, detail="Invalid lead ID in document_id[2]")
    return int(lead_id)
