#import utils as m

import streamlit as st

import main as m
import folium
from streamlit_folium import st_folium, folium_static

# plotting - explore()
import matplotlib
import mapclassify

from collections import defaultdict

st.set_page_config(
    page_title="Gergo Gyori's Bachelor Project - IT University of Copenhagen, Data Science", 
    page_icon="🎄", 
    initial_sidebar_state="collapsed",
    layout="centered",
    menu_items={
        "Report a Bug": "mailto:gergo.gyori@gmail.com"
        "About": "# This page is part of my bachelor project. In case of questions of comment please contact with me: gergo.gyori@gmail.com"
    }
)
st.markdown("# Demo - Check my code")
st.markdown("##### This will be my code for my bachelor project. The goal is to find ideal places to live / visit based on user inputs. ")
st.markdown("##### Here is a demo version. Below the code will show the intersection of all your input. Like: I would like to find every area where: - A pub, a fuel station and a super market is available within 1000 metres ")
st.markdown("### Define a radius in meters around any... ")

# init # maybe the readins should get @st.cache_data ? 

PATH = {}
PATH["processed"] = "data/amenities/processed/"


AMENITIES = ["pubs", "fuelstation", "supermarket", "motorway", "library"]

# load
amenitiesDict = defaultdict(str)
FOCUS = "polygons"
for i in AMENITIES:
    amenitiesDict[str(i+"-"+FOCUS)] = m.gpd.read_parquet(PATH["processed"]+ i + ".parquet")

sliderRange = list(range(10,100, 10))
sliderRange.extend(range(100,1000, 100))
sliderRange.extend(range(1000,10000, 1000))
sliderRange.extend(range(10000,100000, 10000))
sliderRange.extend(range(100000,600000, 25000))


def Update():
    
    #st.spinner(text="Calculation is in progress ...")
    #st.write("updating", radiusPubs, radiusFuel, radiusSP)
    # has to be updated:
    INTEREST = [tb1,tb2,tb3,tb4,tb5]
    RADIUS = [radiusPubs, radiusFuel, radiusSP, radiusHR,radiusLIB]
    #INTEREST = [1,1,1,1,1]
    #RADIUS = [radiusSP,radiusPubs,radiusFuel,3000,3000]
    
    FOCUS = "polygons"
    rankDict = defaultdict(int)
    for inte, rad, amen in zip(INTEREST, RADIUS, AMENITIES):
        if inte == True:
            FOCUS = "polygons"
            # do the thing
            #st.write(amenitiesDict[str(amen+"-"+FOCUS)])
            polyg = m.polygonMakerShapely(amenitiesDict[str(amen+"-"+FOCUS)], diameter=rad, numberOfPoints=30)
            boundary = m.gpd.GeoSeries(m.unary_union(polyg))
            FOCUS = "points"
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
            
    #boundRes.crs = "epsg:4326"
    boundRes.explore()
    #multi1 = m.gpd.GeoSeries([boundRes])
    boundRes.crs = "epsg:4326"
    # multi1.explore() # this doesnt work itself
    
    #st.write(boundRes.head(3))
    #st.write(len(multi1.explode()))
    # multi1.crs = "epsg:4326"
    #multi1 = m.gpd.GeoSeries([boundRes])
    #multi1.crs = "epsg:4326"
    st_map = folium_static(boundRes.explore(), width=1500)
    #st.success('Done!')




form = st.form(key="form_settings")

chkb1, col1 = form.columns([1, 3])
chkb2, col2 = form.columns([1, 3])
chkb3, col3 = form.columns([1, 3])
chkb4, col4 = form.columns([1, 3])
chkb5, col5 = form.columns([1, 3])
# bttn = form.columns([3])



tb1 = chkb1.checkbox('Include', key="tb1", value=True)
radiusPubs = col1.select_slider(
    "... pub",
    options=sliderRange,
    value = 1000,
    key="radiusPubsK",
)

tb2 = chkb2.checkbox('Include', key="tb2", value=True)
radiusFuel = col2.select_slider(
    "... fuel station",
    options=sliderRange,
    value = 1000,
    key="radiusFuelK",
)

tb3 = chkb3.checkbox('Include', key="tb3", value=True)
radiusSP = col3.select_slider(
    "... supermarket",
    options=sliderRange,
    value = 1000,
    key="radiusSupermarket",
)

tb4 = chkb4.checkbox('Include', key="tb4")
radiusHR = col4.select_slider(
    "... highway Ramp",
    options=sliderRange,
    value = 1000,
    key="hiwgwayramp",
)


tb5 = chkb5.checkbox('Include', key="tb5")
radiusLIB = col4.select_slider(
    "... library",
    options=sliderRange,
    value = 1000,
    key="library",
)
st.markdown("### ...and push the submit button")

# it put it into the form
form.form_submit_button("Submit", on_click=Update())

#submitted = st.form_submit_button("Calculations")

#

# transaction_df = transaction_df[transaction_df["list_price"] > standard_cost_slider