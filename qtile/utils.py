#!/usr/bin/python3
import json
from os import getenv

def loadtheme():
    with open(f"{getenv('HOME')}/.config/qtile/theme.json", "r") as config:
        stema = json.load(config)

    with open(f"{getenv('HOME')}/.config/qtile/themes/{stema['theme']}.json", "r") as ftheme:
        tema = json.load(ftheme)
    
    return tema