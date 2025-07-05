import os
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker

engine_ = None
sessionmaker_ = None
async_engine_ = None
async_sessionmaker_ = None


def get_engine(pool_size: int | None = None) -> Engine:
    """Create sqlalchemy engine or return existing"""
    global engine_
    if not engine_:
        kwargs = {"pool_pre_ping": True}
        if pool_size is not None:
            kwargs["pool_size"] = pool_size
        engine_ = create_engine(os.getenv("DB_AUTH_URL"), **kwargs)
    return engine_


def get_sessionmaker() -> sessionmaker:
    """Create sqlalchemy SessionMaker or return existing"""
    global sessionmaker_
    if not sessionmaker_:
        sessionmaker_ = sessionmaker(bind=get_engine())
    return sessionmaker_


def get_async_engine(pool_size: int | None = None) -> AsyncEngine:
    """Create sqlalchemy async engine or return existing"""
    global async_engine_
    if not async_engine_:
        kwargs = {"pool_pre_ping": True}
        if pool_size is not None:
            kwargs["pool_size"] = pool_size
        async_engine_ = create_async_engine(os.getenv("DB_AUTH_URL"), **kwargs)
    return async_engine_


def get_async_sessionmaker() -> async_sessionmaker:
    """Create sqlalchemy async SessionMaker or return existing"""
    global async_sessionmaker_
    if not async_sessionmaker_:
        async_sessionmaker_ = async_sessionmaker(bind=get_async_engine())
    return async_sessionmaker_
