import asyncio
import functools
from collections import defaultdict
from cachetools import Cache
from cachetools.keys import hashkey


def successful_cache(cache: Cache):
    _locks: dict = defaultdict(asyncio.Lock)

    def decorator(func):
        is_async = asyncio.iscoroutinefunction(func)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            key = hashkey(*args, **kwargs)
            result = cache.get(key)
            if result is not None:
                return result

            lock = _locks[key]
            async with lock:
                try:
                    result = cache.get(key)
                    if result is not None:
                        return result
                    result = await func(*args, **kwargs)
                    if result is not None:
                        cache[key] = result
                    return result
                finally:
                    _locks.pop(key, None)

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            key = hashkey(*args, **kwargs)
            result = cache.get(key)
            if result is not None:
                return result
            result = func(*args, **kwargs)
            if result is not None:
                cache[key] = result
            return result

        return async_wrapper if is_async else sync_wrapper

    return decorator
