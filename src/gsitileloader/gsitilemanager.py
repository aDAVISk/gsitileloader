import json
import os
import numpy as np
from requests.exceptions import HTTPError
from xyztilefile import *
from .gsitileloader import GSITileLoader

xyz = calc_xyz_from_lonlat

class GSITileManager(GSITileLoader):
    def __init__(self, key:str, localsrc:str, **kwargs):
        self._cache = {}
        self.localsrc = XYZTileFile(localsrc, cache=self._cache)
        self.httploader = GSITileloader(key,cache=self._cache,**kwargs)
        self.credit = self.httploader.credit
        self.zoomlevels = self.httploader.zoomlevels

    def get(self,lat, lon, zoom, **kwargs):
        if zoom not in self.zoomlevels:
            return None
        try:
            return self.localsrc.get(*xyz(lon,lat,zoom))
        except FileNotFoundError:
            pass
        try:
            return self.httploader.get(*xyz(lon,lat,zoom)) # get the corresponding tile
        except HTTPError:
            pass
        return None

    def __repr__(self):
        return f"<{repr(self.__class__)}: {repr(slef.localsrc)}, {repr(self.httploader)}>"
