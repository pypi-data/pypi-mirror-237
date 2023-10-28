#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from phantasy_rest.routers import mp_router
from phantasy_rest.routers import ca_router
from phantasy_rest.routers import phy_router
from phantasy_rest.routers import misc_router

from phantasy_rest._cache import cache, FASTAPI_CACHE_DISABLED
if not FASTAPI_CACHE_DISABLED:
    from phantasy_rest._cache import FastAPICache
    from phantasy_rest._cache import InMemoryBackend

app = FastAPI()
app.include_router(mp_router.router)
app.include_router(ca_router.router)
app.include_router(phy_router.router)
app.include_router(misc_router.router)

app.mount("/static",  StaticFiles(directory="static"), name='static')

@app.get('/')
@cache(expire=60)
async def index():
    """Get package info.
    """
    import phantasy_rest
    return {
        "Package name": phantasy_rest.__name__,
        "Version": phantasy_rest.__version__,
        "Author": phantasy_rest.__author__,
        "Description": phantasy_rest.__doc__
    }


@app.get('/lattice')
@cache(expire=60)
async def lattice():
    """Get loaded lattice info.
    """
    from phantasy_rest._gconf import machine, segment
    return {"machine": machine, "segment": segment}


@app.get('/config/data')
@cache(expire=60)
async def config_data():
    """Get data path config
    """
    from phantasy_rest._gconf import cav_data_path
    return {"cavity data": cav_data_path}


@app.get('/config')
@cache(expire=60)
async def config():
    """Get gunicorn configurations.
    """
    import subprocess
    import phantasy_rest
    s = subprocess.run("gunicorn --print-config main:app --config _gconf.py".split(),
                       cwd=phantasy_rest.__path__[0],
                       capture_output=True)
    return {
        k.strip(): v.strip()
        for k, v in (i.split("=")
                     for i in s.stdout.decode().strip().split("\n") if '=' in i)
    }


@app.on_event("startup")
async def startup():
    if not FASTAPI_CACHE_DISABLED:
        FastAPICache.init(InMemoryBackend())


@app.get("/clear")
async def clear():
    if not FASTAPI_CACHE_DISABLED:
        return await FastAPICache.clear()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app",
                port=8080,
                host="127.0.0.1",
                reload=True,
                debug=True)
