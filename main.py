import json

import geopandas as gpd

# save resc
import gc

# mapping
import folium
from shapely import geometry
import geog
from shapely.geometry import Polygon

import numpy as np

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
    return polygon