#import utils as m
import streamlit as st

st.set_page_config(
    page_title="Gergo Gyoir's Bachelor Project", page_icon="🎄", initial_sidebar_state="collapsed"
)
st.markdown("# My code is under construction, come back later")

with st.spinner("Load packages..."):
    import mainloc as ml
    import main as m
    import streamlitclasses as stc
    import time


with st.spinner("Load files..."):
    # load
    # init dataset
    PATH = {}
    PATH["processed"] = "data/amenities/processed/"
    AMENITIES = ["supermarket", "pubs", "fuelstation", "motorway", "library"]
    amenitiesDict = m.defaultdict(str)
    FOCUS = "polygons"
    for i in AMENITIES:
        amenitiesDict[str(i+"-"+FOCUS)] = m.gpd.read_parquet(PATH["processed"]+ i + ".parquet")
    
    
col1, col2 = st.columns([1, 3])

def Update():
    with st.echo():
        st.write("This code will be printed to the sidebar.")
        st.write(no2_slider, no2_checkbox, no3_slider, no3_checkbox)
    
# default language
## todo: get it form a button

language = "ENG"

# expander

with col1:
    with st.expander(stc.language[language]["expander-air"]):
        st.write(stc.language[language]["expander-air-description"])
        no2_slider = st.slider('How old are you?', 0, 130, 25, key="no2_slider")
        no2_checkbox = st.checkbox(stc.language[language]["include_button"], key="no2")
    with st.expander(stc.language[language]["expander-air"]):
        st.write(stc.language[language]["expander-air-description"])
        no3_slider = st.slider('How old are you?', 0, 130, 25, key="no3_slider")
        no3_checkbox = st.checkbox(stc.language[language]["include_button"], key="no3")
        

    st.button('Submit', on_click=Update)

