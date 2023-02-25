#import utils as m

import streamlit as st

import main as m
import folium
from streamlit_folium import st_folium, folium_static

# plotting - explore()
import matplotlib
import mapclassify

from collections import defaultdict

# init dataset
PATH = {}
PATH["processed"] = "data/amenities/processed/"

AMENITIES = ["supermarket", "pubs", "fuelstation", "motorway", "library"]

# load
amenitiesDict = defaultdict(str)
FOCUS = "polygons"
for i in AMENITIES:
    amenitiesDict[str(i+"-"+FOCUS)] = m.gpd.read_parquet(PATH["processed"]+ i + ".parquet")

st.set_page_config(
    page_title="simple_init_Gergo Gyoir's Bachelor Project", page_icon="🎄", initial_sidebar_state="collapsed"
)
st.markdown("# My code is under construction, come back later")

# init # maybe the readins should get @st.cache_data ? 

PATH = {}
PATH["processed"] = "data/amenities/processed/"
boundRes = 0

#gdf1 = m.gpd.read_parquet(PATH["processed"]+ "supermarket.parquet")
#gdf2 = m.gpd.read_parquet(PATH["processed"]+ "pubs.parquet")
#gdf3 = m.gpd.read_parquet(PATH["processed"]+ "motorway.parquet")
#gdf4 = m.gpd.read_parquet(PATH["processed"]+ "library.parquet")
#gdf5 = m.gpd.read_parquet(PATH["processed"]+ "fuel.parquet")
#st.write("packages are loaded")

def initFiles():
    
    #st.write("updating", radiusPubs, radiusFuel, radiusSP)
    # has to be updated:
    INTEREST = [tb1,tb2,tb3,tb4,tb5]
    RADIUS = [radiusPubs,radiusFuel,radiusSP,radiusHR,radiusLIB]
    st.write(RADIUS)
    
    FOCUS = "polygons"
    rankDict = defaultdict(int)
    for inte, rad, amen in zip(INTEREST, RADIUS, AMENITIES):
        if inte == 1:
            FOCUS = "polygons"
            # do the thing
            polyg = m.polygonMakerShapely(amenitiesDict[str(amen+"-"+FOCUS)], diameter=rad, numberOfPoints=30)
            boundary = m.gpd.GeoSeries(m.unary_union(polyg))
            FOCUS = "points"
            #boundRes.crs = "epsg:4326"
            amenitiesDict[str(amen+"-"+FOCUS)] = boundary
            FOCUS = "rank"
            rankDict[str(amen)] = int(len(boundary.explode(index_parts=True)))
        else:
            rankDict[str(amen)] = -1
            
    rankDict = {k: v for k, v in sorted(rankDict.items(), key=lambda item: item[1])}
    
    
    # do the multipolygon
    r = 0
    FOCUS = "points"
    for amen in rankDict:
        if rankDict[amen] != - 1:
            if r == 0:
                polyg = amenitiesDict[str(amen+"-"+FOCUS)]
                boundRes = polyg.intersection(polyg)
                r += 1
                # init
            else:
                polyg = amenitiesDict[str(amen+"-"+FOCUS)]
                #display(boundRes.explore())
                boundRes = boundRes.intersection(polyg)
                r += 1
        else:
            None
            
    boundRes.crs = "epsg:4326"
    #boundRes.explore()
    st_map = folium_static(boundRes.explore(), width=1000)



sliderRange = list(range(10,100, 10))
sliderRange.extend(range(100,1000, 100))
sliderRange.extend(range(1000,10000, 1000))
sliderRange.extend(range(10000,100000, 10000))
sliderRange.extend(range(100000,600000, 25000))

map = folium.Map()
tb1,tb2,tb3,tb4,tb5 = 1,1,1,1,1
radiusPubs,radiusFuel,radiusSP,radiusHR,radiusLIB = 3000,3000,3000,3000,3000

initFiles()