#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" EPICS routers """
import json
from typing import Optional, Union, List
from fastapi import APIRouter
from fastapi import Response

router = APIRouter()

try:
    import aioca
    from epicscorelibs.ca.dbr import ca_array
except ModuleNotFoundError:
    print("Install aioca to use CA APIs.")


@router.post("/epics/caget")
async def caget(pvname: Union[List[str], str], datatype: Optional[str] = None):
    """Get the value(s) of PV(s) through CA.
    """
    # datatype: https://dls-controls.github.io/aioca/master/api.html#augmented-values
    if datatype in ("", "none", "None"):
        datatype = None
    results = await aioca.caget(pvname, datatype=datatype)
    rlist = []
    for r in results:
        if isinstance(r, ca_array):
            if datatype == 'str':
                rlist.append(''.join(chr(int(float(i))) for i in r).strip('\x00'))
            else:
                rlist.append(r.tolist())
        else:
            rlist.append(r)
    return Response(content=json.dumps(rlist), media_type='application/json')


@router.post("/epics/caput")
async def caput(pvname: str, value):
    """Set PV with a new value through CA.
    """
    return await aioca.caput(pvname, value, throw=False)

