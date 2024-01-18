import json
import os
from xyztilefile import *

xyz = calc_xyz_from_lonlat

class GSITileLoader:
    with open(os.path.dirname(__file__)+"\\tileinfo.json", "r") as ifile:
        tilelist = json.load(ifile)

    @classmethod
    def search(cls,key):
        for vv in cls.tilelist:
            if vv["tilename"] == key or vv["url"] == key:
                return vv.copy()
        return None

    @classmethod
    def search_about(cls,key):
        res = []
        for vv in cls.tilelist:
            if key in vv["tilename"]:
                res.append(vv.copy())
        return res

    def __init__(self):
        self.loader = XYZTileFile("https://cyberjapandata.gsi.go.jp/xyz/dem5a/{z}/{x}/{y}.txt")

    def get(lon, lat, zoom):
        return loader.get(*xyz(lon,lat,zoom))

    def __repr__(self):
        return f"<{repr(self.__class__)}: {repr(self.loader)}>"
