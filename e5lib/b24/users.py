import os
import logging
from ast import literal_eval

from au_b24 import get_user, get_dep_name


def get_dep_ids(user: dict) -> list[int] | None:
    """Get department IDs from user data."""
    if not user or not isinstance(user, dict):
        return None
    dep_ids = user.get("UF_DEPARTMENT")
    if not dep_ids or not isinstance(dep_ids, list):
        return None
    return dep_ids


def get_dep_id(user: dict) -> int | None:
    """Get department ID from user data."""
    if not user or not isinstance(user, dict):
        return None
    dep_ids = user.get("UF_DEPARTMENT")
    if not dep_ids or not isinstance(dep_ids, list):
        return None
    return dep_ids[0]


def get_dep_name_from_user(
    user_id: int | str | None = None, user: dict | None = None
) -> str | None:
    if isinstance(user_id, dict):
        user = user_id
    user = user or get_user(user_id)
    if not user:
        return None
    dep_id = get_dep_id(user)
    if not dep_id:
        return None
    return get_dep_name(dep_id)


def is_fired(user: dict) -> bool | None:
    if not user or not isinstance(user, dict):
        return
    active = user.get("ACTIVE")
    if active is None:
        return None
    return not user.get("ACTIVE")


def is_in_prohibited_department(user: dict) -> bool | None:
    if not user or not isinstance(user, dict):
        return
    prohibited_dep_ids_raw = os.getenv("PROHIBITED_DEPARTMENT_IDS")
    if not prohibited_dep_ids_raw:
        return None
    try:
        prohibited_dep_ids = literal_eval(prohibited_dep_ids_raw)
    except (ValueError, SyntaxError):
        logging.error("Invalid PROHIBITED_DEPARTMENT_IDS format.")
        return None
    dep_ids = get_dep_ids(user)
    if dep_ids is None:
        return None
    return any(dep_id in prohibited_dep_ids for dep_id in dep_ids)
