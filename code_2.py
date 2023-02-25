#import utils as m

import streamlit as st

import main as m
import folium
from streamlit_folium import st_folium

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
    page_title="Gergo Gyoir's Bachelor Project", page_icon="🎄", initial_sidebar_state="collapsed"
)
st.markdown("# Check my code")

# init # maybe the readins should get @st.cache_data ? 

PATH = {}
PATH["processed"] = "data/amenities/processed/"


#gdf1 = m.gpd.read_parquet(PATH["processed"]+ "supermarket.parquet")
#gdf2 = m.gpd.read_parquet(PATH["processed"]+ "pubs.parquet")
#gdf3 = m.gpd.read_parquet(PATH["processed"]+ "motorway.parquet")
#gdf4 = m.gpd.read_parquet(PATH["processed"]+ "library.parquet")
#gdf5 = m.gpd.read_parquet(PATH["processed"]+ "fuel.parquet")
#st.write("packages are loaded")

def Update():
    
    
    #st.write("updating", radiusPubs, radiusFuel, radiusSP)
    # has to be updated:
    INTEREST = [1,1,1,0,0]
    RADIUS = [radiusPubs,radiusFuel,radiusSP,3021,3000]
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
    boundRes.explore()
    #multi1 = m.gpd.GeoSeries([boundRes])
    #multi1.crs = "epsg:4326"
    # multi1.explore() # this doesnt work itself
    
    st.write(boundRes.head(3))
    #st.write(len(multi1.explode()))
    # multi1.crs = "epsg:4326"
    #multi1 = m.gpd.GeoSeries([boundRes])
    #multi1.crs = "epsg:4326"
    st_map = st_folium(boundRes.explore(), width=1000)
    #st_map = st_folium(multi1, width=800, height=450)




st.write("")
form = st.form(key="form_settings")
col1, col2, col3 = form.columns([1, 1, 1])

radiusPubs = col1.slider(
    "Radius of Pubs",
    1,
    10000,
    1000,
    key="radiusPubsK",
)

radiusFuel = col2.slider(
    "Radius of Fuel",
    1,
    10000,
    1000,
    key="radiusFuelK",
)

radiusSP = col3.slider(
    "Radius of Supermarkets",
    1,
    10000,
    1000,
    key="radiusSPK",
)


# it put it into the form
form.form_submit_button("Submit", on_click=Update())

#submitted = st.form_submit_button("Calculations")

#

# transaction_df = transaction_df[transaction_df["list_price"] > standard_cost_slider