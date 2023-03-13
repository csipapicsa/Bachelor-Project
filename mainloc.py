# risky import
from collections import defaultdict

#developmemnt
import importlib as i


import json

import geopandas as gpd
import pandas as pd
import matplotlib
import mapclassify

# save resc
import gc
import pyarrow.parquet as pq

# mapping
import folium
from shapely import geometry
import geog
from shapely.geometry import Polygon

# multipolygon maker
from shapely.ops import unary_union

import numpy as np

# reading
import xarray as xr

# polygon expander
from shapely.ops import transform
from functools import partial
import pyproj

links = ["https://docs.google.com/document/d/1nJNTRmol4ymWYo0FJfWdZ3azY0MA1GzLiD9Hzr54dY0/edit", "https://docs.google.com/document/d/127Fu-z-c_WAIfmnDXootdAbibFylmHP0hJhB4WWNUVo/edit"]



def saveGPS(file, filename=""):
    """
    save geopandas file to json object
    """
    file = file.to_json()
    json_object = json.loads(file)
    json_object = json.dumps(json_object)
    # save it 
    with open(str("rawPoints/"+filename+".json"), "w") as outfile:
        outfile.write(json_object)
    # cleaning
    outfile.close()
    del file
    gc.collect()
    return None


def openJSON(filename=""):
    """
    open geopandas file from json object
    """
    file = open(str("rawPoints/"+filename+".json"))
    fileR = json.load(file)
    gdf = gpd.GeoDataFrame.from_features(fileR["features"])
    # gdf.crs = "EPSG:23700" #Hungary, but doesnt wokr when I wanna explore
    gdf.crs = "epsg:4326"
    file.close()
    # cleaning
    del fileR
    gc.collect()
    return gdf
    
def multiPolygonVisualizer(file, color='blue'):
    """
    takes a multipolygon as "file" and plot it
    """
    ma = folium.Map([47.762196497129665, 19.6742448729209], zoom_start=7)
    sim_geo = gpd.GeoSeries(file) # without 
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j,
                       style_function=lambda x: {'fillColor': color,
                                                'weight': 0})
    geo_j.add_to(ma)
    display(ma)
    return None
    
def polygonMakerShapely(datab, diameter, numberOfPoints=100):
    """ 
    Make a sircle around a point.
    Note: It make a circle around the middle of polygons, not around the edges of the building
    """
    polygon = [] # collect polygons
    angles = np.linspace(0, 360, numberOfPoints) # calculate circle area around a point 
    datab["geometry"] = datab.centroid # get the center of all type geometries
    for coordinates in datab["geometry"]:
        poly = geometry.Polygon(geog.propagate([coordinates.x, coordinates.y], angles, diameter))
        polygon.append(poly)
    # new 19.02.2023 -- since we return the whole db, it is slower. 
    datab = gpd.GeoDataFrame(geometry=polygon)
    datab.crs = "epsg:4326"
    # datab["geometry"] = polygon
    return datab
    
def pointMaper(df, fileType="pandas"):

    ma = folium.Map([47.762196497129665, 19.6742448729209], zoom_start=7)
    for i, r in df.iterrows():
        folium.Marker(location=[r.LATITUDE, r.LONGITUDE], fill_color='#43d9de', radius=8 ).add_to(ma)
    display(ma)
    
    
# polygon expander for Hungary

def polygonExpander(data, diameter=0):
    # since we are focusing on Hungary
    # init
    hun_crs = "EPSG:23700"
    global_crs = "EPSG:4326"
    
    data = data.to_crs(hun_crs) # has to project for proper expansion
    l = list(data.geometry) # get the geometries
    
    project = partial(
    pyproj.transform,
    pyproj.Proj(hun_crs), # source coordinate system (WGS 84)
    pyproj.Proj(hun_crs)  # target coordinate system (Web Mercator)
                                )

    newValues = []
    for i in l:
        newValues.append(transform(project, i).buffer(diameter))
                       
    data.geometry = newValues
    data = data.to_crs(global_crs) # convert back to normal GPS

    return data