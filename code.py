#import utils as m
import streamlit as st
import main as m
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Gergo Gyoir's Bachelor Project", page_icon="🎄", initial_sidebar_state="collapsed"
)
st.markdown("# Check my code")

# init # maybe the readins should get @st.cache_data ? 
gdf1 = m.openJSON(filename="pubs")
gdf2 = m.openJSON(filename="fuel")
gdf3 = m.openJSON(filename="supermarket")

def Update():
    
    print("diameter", radiusPubs)
    polyg1 = m.polygonMakerShapely(gdf1, diameter=radiusPubs, numberOfPoints=50)
    polyg2 = m.polygonMakerShapely(gdf2, diameter=radiusFuel, numberOfPoints=50)
    polyg3 = m.polygonMakerShapely(gdf3, diameter=radiusSP, numberOfPoints=50)
    
    
    polyg1 = polyg1.geometry.unary_union
    polyg2 = polyg2.geometry.unary_union
    polyg3 = polyg3.geometry.unary_union
    
    # todo: do it in order
    boundRes = polyg1.intersection(polyg2)
    boundRes = boundRes.intersection(polyg3)
    #boundRes.explore()
    
    # must to have part
    multi1 = m.gpd.GeoSeries([boundRes])
    multi1.crs = "epsg:4326"
    # multi1.explore() # this doesnt work itself
    
    st.write(multi1.head(3))
    #st.write(len(multi1.explode()))
    # multi1.crs = "epsg:4326"
    #multi1 = m.gpd.GeoSeries([boundRes])
    #multi1.crs = "epsg:4326"
    st_map = st_folium(multi1.explore(), width=1000)
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



'''if st.button('Calculation'):
    gdf1 = m.openJSON(filename="pubs")
    print("diameter", radiusPubs)
    polyg1 = m.polygonMakerShapely(gdf1, diameter=radiusPubs, numberOfPoints=50)
    polyg1 = polyg1.geometry.unary_union
    multi1 = m.gpd.GeoSeries([polyg1])
    multi1.explore()
    st.write(radiusPubs)
    st.write(len(multi1.explode()))
    ma = folium.Map()
    st_map = st_folium(ma)
    # do the calculation
'''
#

# transaction_df = transaction_df[transaction_df["list_price"] > standard_cost_slider