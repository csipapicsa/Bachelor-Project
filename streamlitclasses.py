### streamlit class
import streamlit as st

## Descriptions
language = {}
language["DESCRIPTIONS"] = {}
language["DESCRIPTIONS"]["welcome"] = {}
language["DESCRIPTIONS"]["welcome"]["ENG"] = {}
language["DESCRIPTIONS"]["welcome"]["ENG"] = "Hello bello"

# expanders 
language["ENG"] = {}
language["HUN"] = {}
language["ENG"]["expander-air"] = "Air quality criterias"
language["HUN"]["expander-air"] = "Levegőminőség kritériák"
language["ENG"]["expander-air-description"] = "Please choose the criterias"
language["HUN"]["expander-air-description"] = "Kérjük válasszon az alábbi kritériák közül"
language["ENG"]["include_button"] = "Include"
language["HUN"]["include_button"] = "Tartalmazza"

## Classes
# slider init
streamlitClass =  {}

sliderRange = list(range(10,100, 10))
sliderRange.extend(range(100,1000, 100))
sliderRange.extend(range(1000,10000, 1000))
sliderRange.extend(range(10000,100000, 10000))
sliderRange.extend(range(100000,600000, 25000))

streamlitClass["RangeAmenities"] = sliderRange

sliderForestRanges = [100,200,300,400,500,600,700,800,900,1000,1500,2000,3000,
          4000,5000,6000,7000,8000,9000,10000,15000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

streamlitClass["RangeAmenities"] = sliderForestRanges

# available databases
# init dataset
PATH = {}
PATH["processed"] = "data/amenities/processed/"

AMENITIES = ["supermarket", "pubs", "fuelstation", "motorway", "library"]

#AIRMEASURES = ["NO2", "O3", "CO", "PM10", "PM25", "OVERALL"]
AIRMEASURES = ["NO2", "O3", "CO", "PM10", "PM25"]

# weather      
            
def sliderMaker(opt):
    ccc = st.select_slider('How old are you?', 
            options=opt,
            value="Good",
            key="PM25_slider")
    return ccc
    
