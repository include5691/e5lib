import os
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

engine_ = None
sessionmaker_ = None

def get_engine() -> Engine:
    """Create sqlalchemy engine or return existing"""
    global engine_
    if not engine_:
        engine_ = create_engine(os.getenv("DB_AUTH_URL"), pool_pre_ping=True)
    return engine_

def get_sessionmaker() -> sessionmaker:
    """Create sqlalchemy SessionMaker or return existing"""
    global sessionmaker_
    if not sessionmaker_:
        sessionmaker_ = sessionmaker(bind=get_engine())
    return sessionmaker_