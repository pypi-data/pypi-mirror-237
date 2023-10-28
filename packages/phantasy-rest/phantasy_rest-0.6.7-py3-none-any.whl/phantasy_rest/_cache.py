try:
    from fastapi_cache import FastAPICache
    from fastapi_cache.decorator import cache
    from fastapi_cache.backends.inmemory import InMemoryBackend
except ModuleNotFoundError:
    print("'fastapi-cache2' is not available, disable caching.")
    FASTAPI_CACHE_DISABLED = True
    def cache(*args, **kws):
        def _wrapper(func):
            return func
        return _wrapper
else:
    FASTAPI_CACHE_DISABLED = False
