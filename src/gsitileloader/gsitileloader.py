import json
import os
import numpy as np
from xyztilefile import *
from requests.exceptions import HTTPError

xyz = calc_xyz_from_lonlat

class GSITileLoader:
    with open(os.path.dirname(__file__)+"/tileinfo.json", "r") as ifile:
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
            if key in vv["tilename"] or key in vv["url"]:
                res.append(vv.copy())
        return res

    def __init__(self, key, cache=None, **kwargs):
        tileinfo = self.__class__.search(key)
        if tileinfo is None:
            raise ValueError(f"No tile is found with {key}")
        self.tileinfo = tileinfo
        #print(kwargs)
        if "required" in self.tileinfo["permission"]:
            if "override_permission" not in kwargs or not kwargs["override_permission"]:
                permission = self.tileinfo["permission"]
                raise RuntimeError(f"This tile has requirements: {permission}.\n If you have fullfilled the requirements, please construct the instance with the keyword 'override_permission=True'.")

        self.loader = XYZTileFile(self.tileinfo["url"].format(**kwargs,x="{x}",y="{y}",z="{z}"),cache=cache)
        self.credit = self.tileinfo["credit"].format(tilename=self.tileinfo["tilename"])
        zoomlevels_len = len(self.tileinfo["zoomlevels"])
        if zoomlevels_len == 2:
            self.zoomlevels = np.arange(self.tileinfo["zoomlevels"][0],self.tileinfo["zoomlevels"][1]+1)
        else:
            self.zoomlevels = np.array(self.tileinfo["zoomlevels"])

    def get(self,lat, lon, zoom, **kwargs):
        if zoom not in self.zoomlevels:
            return None
        try:
            return self.loader.get(*xyz(lon,lat,zoom)) # get the corresponding tile
        except HTTPError:
            return None

    def __repr__(self):
        return f"<{repr(self.__class__)}: {repr(self.loader)}, credit: {repr(self.credit)}, zoomlevels:{repr(self.zoomlevels)}>"
