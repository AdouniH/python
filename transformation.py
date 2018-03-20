# -*- coding: utf-8 -*-


# longlat --> x,y

from pyproj import Proj,transform

WGS = Proj(init='epsg:4326')
WGS_UTM_32N = Proj(init='epsg:32632')
longitude=10.1
latitude=36.8
x2, y2 = transform(WGS,WGS_UTM_32N,longitude,latitude)

print(x2)
print(y2)


