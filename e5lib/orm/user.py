import time
from sqlalchemy import Column, Integer, String, Boolean


class User:
    """A mixin class to handle user data denormalization in ORM models"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer, nullable=False)
    name = Column(String(50))
    dep_id = Column(Integer)
    dep_name = Column(String(50))
    is_fired = Column(Boolean, server_default="false", nullable=False)

    def __init__(
        self,
        id: int,
        name: str,
        dep_id: int,
        dep_name: str,
        timestamp: int | float = time.time(),
        is_fired: bool = False,
    ):
        self.id = id
        if name:
            self.name = name[:50]
        self.dep_id = dep_id
        if dep_name:
            self.dep_name = dep_name[:50]
        self.timestamp = int(timestamp)
        self.is_fired = is_fired
