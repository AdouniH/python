# -*- coding: utf-8 -*-


# longlat --> x,y

from pyproj import Proj,transform

WGS = Proj(init='epsg:4326')
WGS_UTM_32N = Proj(init='epsg:32632')
long=10.1
lat=36.8
x2, y2 = transform(WGS,WGS_UTM_32N,long,lat)
"""
print(x2)
print(y2)
"""

