#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import hashlib
import pandas as pd
import os

templates = Jinja2Templates(directory="./templates")
router = APIRouter()

# md5 of cavity data file.
CAV_DATA_MD5 = ""


@router.get("/data/cavity")
async def get_cav_data():
    """ Return cavity field data in JSON. """
    from phantasy_rest._gconf import cav_data_path as _path
    df = pd.read_csv(os.path.expanduser(_path))
    return df.to_json()


@router.get("/table/cavity", response_class=HTMLResponse)
async def get_cav_table(request: Request):
    """ Present cavity field data in a table. """
    from phantasy_rest._gconf import cav_data_path as _path
    with open(os.path.expanduser(_path), "r") as fp:
        ts = fp.readline().strip("#\ \n")
        df = pd.read_csv(fp)
        df.insert(0, "#", df.index)
    columns = df.columns
    rows = df.to_dict(orient="records")
    return templates.TemplateResponse("table.html", {
        "request": request,
        "columns": columns,
        "rows": rows,
        "pageName": "SRF Cavity Field Data",
        "retrieved_datetime": ts,
        "refresh_interval": 1800,
    })

@router.get("/data-utils/is_cavity_data_new")
async def is_cav_data_new():
    """ Return if the cavity field data is new or not.
    """
    global CAV_DATA_MD5
    from phantasy_rest._gconf import cav_data_path as _path
    with open(os.path.expanduser(_path), "r") as fp:
        md5_now = hashlib.md5(fp.read().encode('utf-8')).hexdigest()
    if md5_now != CAV_DATA_MD5:
        CAV_DATA_MD5 = md5_now
        return True
    else:
        return False
