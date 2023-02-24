#import utils as m
import streamlit as st


st.set_page_config(
    page_title="Gergo Gyoir's Bachelor Project", page_icon="🎄", initial_sidebar_state="collapsed"
)
st.markdown("# Check my code")

st.write("")
form = st.form(key="form_settings")
radiusPubs, radiusFuel, radiusSP = form.columns([1, 1, 1])

radiusPubs = col1.slider(
    "Radius of Pubs",
    1,
    100000,
    key="radiusPubsK",
)

radiusFuel = col1.slider(
    "Radius of Fuel",
    1,
    100000,
    key="radiusFuelK",
)

radiusSP = col1.slider(
    "Radius of Supermarkets",
    1,
    100000,
    key="radiusSPK",
)

with st.spinner("Creating map... (may take up to a minute)"):
    # loading
    None


if st.button('Calculation'):
    gdf1 = m.openJSON(filename="rawpPoints/pubs.json")
    polyg1 = m.polygonMakerShapely(gdf1, diameter=radiusPubs, numberOfPoints=50)
    polyg1 = polyg1.geometry.unary_union
    multi1 = m.gpd.GeoSeries([polyg1])
    st.write(len(multi1))
    # do the calculation
else:
    st.write('Goodbye')

#


# transaction_df = transaction_df[transaction_df["list_price"] > standard_cost_slider