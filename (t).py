# coding: utf-8
# load
# https://gis.stackexchange.com/questions/237053/getting-intersection-of-multiple-polygons-efficiently-in-python# mapping
import folium
import osmnx as ox
import numpy

# timing
import time

import sys

# save databases
import json
import geopandas as gpd
import fiona
# get some points
# dummy coffee point
start = time.time()
# define what we wanna see
tags = {'amenity': 'pub'}
# define where

# when its Hungary it takes a lot of time 
# better to save it 
place = "Hungary"

# doesnt work with Selyp
# place = "Lorinci, Hungary"
cafe = ox.geometries_from_place(place, tags=tags)
end = time.time()
print(end - start)
type(cafe)
import main as m
# load
# https://gis.stackexchange.com/questions/237053/getting-intersection-of-multiple-polygons-efficiently-in-python# mapping
import folium
import osmnx as ox
import numpy

# timing
import time

import sys

# save databases
import json

#reload
import imp as i
# load
# https://gis.stackexchange.com/questions/237053/getting-intersection-of-multiple-polygons-efficiently-in-python# mapping
import folium
import osmnx as ox
import numpy

# timing
import time

import sys

# save databases
import json

#reload
import importlib as i
i.reload(main)
i.reload(m)
import main as m
m.saveGPS(cafe, filename="pubs")
i.reload(m)
import main as m
m.saveGPS(cafe, filename="pubs")
import main as m
i.reload(m)
m.saveGPS(cafe, filename="pubs")
i.reload(m)
i.reload(m)
# open a file
gdf = m.openJSON(pubs)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
gdf
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# save it to json file
m.saveGPS(cafe, filename="pubs")
i.reload(m)
# save it to json file
m.saveGPS(cafe, filename="pubs")
i.reload(m)
# save it to json file
m.saveGPS(cafe, filename="pubs")
i.reload(m)
# save it to json file
m.saveGPS(cafe, filename="pubs")
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# open a file
gdf = m.openJSON(filename="pubs")
i.reload(m)
# save it to json file
m.saveGPS(cafe, filename="pubs")
# open a file
gdf = m.openJSON(filename="pubs")
gdf
polyg = polygonMakerShapely(gdf, diameter=3000)
# create a circle around the points
import numpy as np
import json
import geog
import shapely.geometry

from shapely import geometry

def polygonMaker(coordinates, diameter, numberOfPoints=100):
    # init polygons
    polygon = []
    angles = np.linspace(0, 360, numberOfPoints)
    for longlat in coordinates:
        polygon.append(geog.propagate(longlat, angles, diameter))
    return polygon

# below works

def polygonMakerShapely(datab, diameter, numberOfPoints=100):
    # init polygons
    polygon = []
    angles = np.linspace(0, 360, numberOfPoints)
    for coordinates in gdf["geometry"]:
        if coordinates.__geo_interface__["type"] == "Point":
            #poly
            poly = geometry.Polygon(geog.propagate([coordinates.x, coordinates.y], angles, diameter))
            polygon.append(poly)
        else:
            # print(coordinates.__geo_interface__["coordinates"][0][0]) # it is a really fucking hack
            poly = geometry.Polygon(geog.propagate(coordinates.__geo_interface__["coordinates"][0][0], angles, diameter))
    return polygon
#print(json.dumps(shapely.geometry.mapping(shapely.geometry.Polygon(polygon))))
polyg = polygonMakerShapely(gdf, diameter=3000)
m = folium.Map([47.762196497129665, 19.6742448729209], zoom_start=7)
# plot the pubs
m = folium.Map([47.762196497129665, 19.6742448729209], zoom_start=7)

for r in polyg:
    # Without simplifying the representation of each borough,
    # the map might not be displayed
    #sim_geo = gpd.GeoSeries(r.simplify(tolerance=0.001)) # it simplifies a lot the given polygon, not good
    sim_geo = gpd.GeoSeries(r) # without 
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j,
                           style_function=lambda x: {'fillColor': 'orange'})
    geo_j.add_to(m)
m
# plot boundary
from shapely.ops import unary_union
# polygon circles to boundary
boundary = gpd.GeoSeries(unary_union(polyg))
boundary
m = folium.Map([47.762196497129665, 19.6742448729209], zoom_start=7)

sim_geo = gpd.GeoSeries(boundary) # without 
geo_j = sim_geo.to_json()
geo_j = folium.GeoJson(data=geo_j,
                       style_function=lambda x: {'fillColor': 'orange'})
geo_j.add_to(m)
m
m = folium.Map([47.762196497129665, 19.6742448729209], zoom_start=7)

sim_geo = gpd.GeoSeries(boundary) # without 
geo_j = sim_geo.to_json()
geo_j = folium.GeoJson(data=geo_j,
                       style_function=lambda x: {'fillColor': 'orange'
                                                "weight": 0})
geo_j.add_to(m)
m
m = folium.Map([47.762196497129665, 19.6742448729209], zoom_start=7)

sim_geo = gpd.GeoSeries(boundary) # without 
geo_j = sim_geo.to_json()
geo_j = folium.GeoJson(data=geo_j,
                       style_function=lambda x: {'fillColor': 'orange',
                                                'weight': 0})
geo_j.add_to(m)
m
m = folium.Map([47.762196497129665, 19.6742448729209], zoom_start=7)

sim_geo = gpd.GeoSeries(boundary) # without 
geo_j = sim_geo.to_json()
geo_j = folium.GeoJson(data=geo_j,
                       style_function=lambda x: {'fillColor': 'blue',
                                                'weight': 0})
geo_j.add_to(m)
m
polyg[1]
polyg[0]
boundary[0]
boundary[1]
t = boundary[0].simplify()
t = boundary[0].simplify(tolerance=0.001)
sys.getsizeof(t)
t.___sizeof___
t.___sizeof___()
t.__sizeof__()
t
