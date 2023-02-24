def openJSON(filename=""):
    """
    open geopandas file from json object
    """
    file = open(filename)
    fileR = json.load(file)
    gdf = gpd.GeoDataFrame.from_features(fileR["features"])
    # gdf.crs = "EPSG:23700" #Hungary, but doesnt wokr when I wanna explore
    gdf.crs = "epsg:4326"
    file.close()
    # cleaning
    del fileR
    return gdf

def polygonMakerShapely(datab, diameter, numberOfPoints=100):
    """ 
    Make a sircle around a point.
    Note: It make a circle around the middle of polygons, not around the edges of the building
    """
    polygon = [] # collect polygons
    angles = np.linspace(0, 360, numberOfPoints) # calculate circle area around a point
    datab.crs = "epsg:4326"
    datab = datab.to_crs(crs=4326)
    # !!!!!!!!!!!!!!!! totally different
    datab["geometry"] = datab.to_crs('+proj=cea').centroid.to_crs(datab.crs) # get the center of all type geometries
    for coordinates in datab["geometry"]:
        poly = geometry.Polygon(geog.propagate([coordinates.x, coordinates.y], angles, diameter))
        polygon.append(poly)
    # new 19.02.2023 -- since we return the whole db, it is slower. 
    datab = gpd.GeoDataFrame(geometry=polygon)
    datab.crs = "epsg:4326"
    # datab["geometry"] = polygon
    return datab

print("imports started")
import json


import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])
 
install(geog)
    
import numpy as np
import geog
from shapely import geometry
print("before geopandas")
import geopandas as gpd