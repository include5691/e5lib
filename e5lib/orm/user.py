from sqlalchemy import Column, Integer, String

class User:
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    dep_id = Column(Integer)
    dep_name = Column(String(50))

    def __init__(self, id, name, dep_id, dep_name):
        self.id = id
        if name:
            self.name = name[:50]
        self.dep_id = dep_id
        if dep_name:
            self.dep_name = dep_name[:50]