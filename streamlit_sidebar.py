#import utils as m
import streamlit as st

st.set_page_config(
    page_title="Gergo Gyoir's Bachelor Project", page_icon="🎄", initial_sidebar_state="collapsed",layout='wide'
)

st.markdown("# My code is under construction, come back later")

with st.spinner("Load packages..."):
    import mainloc as ml
    import main as m
    import streamlitclasses as stc
    import time


with st.spinner("Mi a faszom..."):
    # load
    # init dataset
    PATH = {}
    PATH["processed"] = "data/amenities/processed/"
    AMENITIES = ["supermarket", "pubs", "fuelstation", "motorway", "library"]
    amenitiesDict = m.defaultdict(str)
    FOCUS = "polygons"
    for i in stc.AMENITIES:
        amenitiesDict[str(i+"-"+FOCUS)] = m.gpd.read_parquet(PATH["processed"]+ i + ".parquet")
        
    PATH["weather"] = "data/weather/unprocessed/"
    PATH["weather-processed"] = "data/weather/processed/"
    airqualityDict = m.defaultdict(str)
    airqualityRanges = m.defaultdict(int)
    
    for i in stc.AIRMEASURES:
        airqualityDict[i] = m.gpd.read_parquet(PATH["weather-processed"]+ i + ".parquet")
        airqualityDict[i].head(10)
        #st.write("air")
        #st.write(i)
        # range of air quality
        try:
            l = set(airqualityDict[i]["QualityString"])
            airqualityRanges[i] = l
            #st.write(l)
        except:
            None
st.success('Done!')   
    
    
    
col1, col2 = st.columns([1, 3])

def Update():
    st.write("This code will be printed to the sidebar.")
    #st.write(no2_slider, no2_checkbox, o3_slider, O3_checkbox)
    
# default language
## todo: get it form a button

language = "ENG"

# expander

# AIRMEASURES = ["NO2", "O3", "CO", "PM10", "PM25", "OVERALL"]

with col1:
    with st.expander(stc.language[language]["expander-air"]):
        st.write(stc.language[language]["expander-air-description"])
        no2_slider = st.select_slider('NO2', 
            options=list(airqualityRanges["NO2"]), 
            value="Good",
            key="NO2_slider")
        no2_checkbox = st.checkbox(stc.language[language]["include_button"], key="no2")

        st.write(stc.language[language]["expander-air-description"])
        o3_slider = st.select_slider('How old are you?', 
            options=["Good", "Faszom"],
            value="Good",
            key="O3_slider")
        O3_checkbox = st.checkbox(stc.language[language]["include_button"], key="no3")
    

        #st.write(stc.language[language]["expander-air-description"])
        #pm25_slider = stc.sliderMaker(airqualityRanges["PM25"])
        #pm25_checkbox = st.checkbox(stc.language[language]["include_button"], key="PM25")
        

    st.button('Submit', on_click=Update())

