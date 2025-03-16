from cachetools import Cache
from cachetools.keys import hashkey

def successful_cache(cache: Cache):
    "Caches only not None results"
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = hashkey(func, *args, **kwargs)
            if key in cache:
                return cache[key]
            result = func(*args, **kwargs)
            if result is not None:
                cache[key] = result
            return result
        return wrapper
    return decorator