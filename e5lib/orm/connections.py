import os
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker

DB_URL = os.getenv("DB_URL") or os.getenv("DB_AUTH_URL")

engine_ = None
sessionmaker_ = None
async_engine_ = None
async_sessionmaker_ = None


def get_engine(db_url: str | None = None, pool_size: int | None = None) -> Engine:
    """Create sqlalchemy engine or return existing"""
    global engine_
    if not engine_:
        kwargs = {"pool_pre_ping": True}
        if pool_size is not None:
            kwargs["pool_size"] = pool_size
        db_url = db_url or DB_URL
        engine_ = create_engine(db_url, **kwargs)
    return engine_


def get_sessionmaker(db_url: str | None = None) -> sessionmaker:
    """Create sqlalchemy SessionMaker or return existing"""
    global sessionmaker_
    if not sessionmaker_:
        db_url = db_url or DB_URL
        sessionmaker_ = sessionmaker(bind=get_engine(db_url))
    return sessionmaker_


def get_async_engine(
    db_url: str | None = None, pool_size: int | None = None
) -> AsyncEngine:
    """Create sqlalchemy async engine or return existing"""
    global async_engine_
    if not async_engine_:
        kwargs = {"pool_pre_ping": True}
        if pool_size is not None:
            kwargs["pool_size"] = pool_size
        db_url = db_url or DB_URL
        async_engine_ = create_async_engine(db_url, **kwargs)
    return async_engine_


def get_async_sessionmaker(db_url: str | None = None) -> async_sessionmaker:
    """Create sqlalchemy async SessionMaker or return existing"""
    global async_sessionmaker_
    if not async_sessionmaker_:
        db_url = db_url or DB_URL
        async_sessionmaker_ = async_sessionmaker(bind=get_async_engine(db_url))
    return async_sessionmaker_
