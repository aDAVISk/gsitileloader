from xyztilefile import *

xyz = calc_xyz_from_lonlat

class GSITileLoader:
    def __init__(self):
        self.loader = XYZTileFile("https://cyberjapandata.gsi.go.jp/xyz/dem5a/{z}/{x}/{y}.txt")

    def get(lon, lat, zoom):
        return loader.get(*xyz(lon,lat,zoom))

    def __repr__(self):
        return f"<{repr(self.__class__)}: {repr(self.loader)}>"
