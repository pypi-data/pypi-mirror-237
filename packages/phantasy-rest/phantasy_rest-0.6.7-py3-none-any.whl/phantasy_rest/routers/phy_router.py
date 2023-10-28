#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Physics functions.
"""
from fastapi import APIRouter

try:
    import atima
except:
    print("Install atima to use physics APIs.")

router = APIRouter()

@router.post("/physics/atima/calc")
async def calc(projectile: dict, material: dict) -> dict:
    """Calculate energy loss when *projectile* passes through *material*.
    """
    # example:
    # curl -X 'POST' <url>/physics/atima/calc \
    #        -H 'accept: application/json' \
    #        -H 'Content-Type: application/json' \
    #        -d '{
    #            "projectile": {"Z": 92, "A": 238.05, "Ek": 1000},
    #            "material": {"Z": 29, "A": 63.546, "thickness": 1000}
    #        }'
    #
    # returns:
    # {"dE/dx":14.518020957575775,    # dE/dx at the entrance, MeV/(mg/cm^2)
    #  "Ek":938.6861572265625,        # Exit energy, MeV/u
    #  "Ek_std":0.28665739306630367,  # Standard deviation of exit energy straggling, MeV/u
    #  "range_in":12594.828498268274, # Stopping range for the initial energy, mg/cm^2
    #  "range_out":11594.827896465355,# Stopping range for the exit energy, mg/cm^2
    #  "range_std":11.898672264037165, # Standard deviation of the stopping range for initial energy, mg/cm^2
    #  "angle_std":1.0524071985855699, # Standard deviation of the angular straggling, mrad
    #  "q_in":91.76187896728516,   # Q-mean for the initial energy
    #  "q_out":91.74201202392578}  # Q-mean for the exit energy
    try:
        projectile['Z'] = int(projectile['Z'])
        material['Z'] = int(material['Z'])
        r = atima.calc(projectile, material)
    except:
        r = {}
    finally:
        return r
