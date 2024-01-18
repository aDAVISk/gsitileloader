# gsitileloader
Loading XYZ tile from The Geospatial Information Authority of Japan (GSI).


### code example
#### Searching tiles
```
from gsitileloader import *
# Searching tiles with keyword
print(GSITileLoader.search_about("標高"))
# Find exact match of tilename or url with keyword
print(GSITileLoader.search('https://cyberjapandata.gsi.go.jp/xyz/lakedepth/{z}/{x}/{y}.png'))
```

#### Fetching a tile
```
from gsitileloader import *
import matplotlib.pyplot as plt
tile3 = GSITileLoader("年代別の写真：年度別空中写真（2007年以降）",year=2021)
img = tile3.get(34.563015,135.487089,16)
fig, ax = plt.subplots()
ax.imshow(img)
plt.show()
```
