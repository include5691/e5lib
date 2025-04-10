import time
from sqlalchemy import Column, Integer, String

class User:
    """A mixin class to handle user data denormalization in ORM models"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer, nullable=False)
    name = Column(String(50))
    dep_id = Column(Integer)
    dep_name = Column(String(50))

    def __init__(self, id: str | int, name: str, dep_id: str | int, dep_name: str, timestamp: int | float = time.time()):
        self.id = id
        self.timestamp = int(timestamp)
        if name:
            self.name = name[:50]
        self.dep_id = dep_id
        if dep_name:
            self.dep_name = dep_name[:50]