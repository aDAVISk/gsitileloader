from gsitileloader import *
import os
import pprint
pp = pprint.PrettyPrinter(indent=3)

tile = GSITileLoader()
pp.pprint(tile)

pp.pprint(GSITileLoader.tilelist)
print("---")
pp.pprint(GSITileLoader.search_about("標高"))
print("---")
pp.pprint(GSITileLoader.search('https://cyberjapandata.gsi.go.jp/xyz/lakedepth/{z}/{x}/{y}.png'))
