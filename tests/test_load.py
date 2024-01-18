from gsitileloader import *
import os
import pprint
pp = pprint.PrettyPrinter(indent=3)

pp.pprint(GSITileLoader.tilelist)
print("---")
pp.pprint(GSITileLoader.search_about("標高"))
print("---")
pp.pprint(GSITileLoader.search('https://cyberjapandata.gsi.go.jp/xyz/lakedepth/{z}/{x}/{y}.png'))
print("---")
tile = GSITileLoader('https://cyberjapandata.gsi.go.jp/xyz/lakedepth/{z}/{x}/{y}.png')
pp.pprint(tile)
print("---")
try:
    tile2 = GSITileLoader('標高')
except ValueError as e:
    print("Error is raised as expected:")
    print(e)
print("---")
try:
    tile2 = GSITileLoader('ベースマップ：標準地図')
except RuntimeError as e:
    print("Error is raised as expected:")
    print(e)
