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

def Update():
    
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



sliderRange = list(range(10,100, 10))
sliderRange.extend(range(100,1000, 100))
sliderRange.extend(range(1000,10000, 1000))
sliderRange.extend(range(10000,100000, 10000))
sliderRange.extend(range(100000,600000, 25000))

st.write("")

formm = st.form(key="form_settings")

chkb1, col1 = formm.columns([1, 3])




chkb2, col2 = formm.columns([1, 3])
chkb3, col3 = formm.columns([1, 3])
chkb4, col4 = formm.columns([1, 3])
chkb5, col5 = formm.columns([1, 3])
# bttn = form.columns([3])



tb1 = chkb1.checkbox('I agree', key="tb1")
radiusPubs = col1.select_slider(
    "Access for a pub",
    options=sliderRange,
    value = 1000,
    key="radiusPubsK",
)

tb2 = chkb2.checkbox('I agree', key="tb2")
radiusFuel = col2.select_slider(
    "Access for a Fuel station",
    options=sliderRange,
    value = 1000,
    key="radiusFuelK",
)

tb3 = chkb3.checkbox('I agree', key="tb3")
radiusSP = col3.select_slider(
    "Access for a supermarket",
    options=sliderRange,
    value = 1000,
    key="radiusSupermarket",
)

tb4 = chkb4.checkbox('I agree', key="tb4")
radiusHR = col4.select_slider(
    "Access for a Highway Ramp",
    options=sliderRange,
    value = 1000,
    key="hiwgwayramp",
)


tb5 = chkb5.checkbox('I agree', key="tb5")
radiusLIB = col4.select_slider(
    "Access for a Library",
    options=sliderRange,
    value = 1000,
    key="library",
)
bt1 = st.button(
    "test1",
    key=None,
    help="help info",
    on_click=Update,
    kwargs=None,
    disabled=False,
)
# it put it into the form
# submit = form.form_submit_button("Submit")

  
st.write("Outside the form")

'''c = 0
if submit:
    with st.spinner(" Calclating ..... "):
        Update()
        st.write(submit)
        c += 1
else:
    st.write(submit)
    if c == 1:
        st_map = st_folium(boundRes.explore(), width=1000)'''
# submitted = st.form_submit_button("Calculations")

formm.form_submit_button("Submit", on_click = Update())


#

# transaction_df = transaction_df[transaction_df["list_price"] > standard_cost_slider