### streamlit class

## Descriptions
language = {}
language["DESCRIPTIONS"] = {}
language["DESCRIPTIONS"]["welcome"] = {}
language["DESCRIPTIONS"]["welcome"]["ENG"] = {}
language["DESCRIPTIONS"]["welcome"]["ENG"] = "Hello bello"

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
amenities = {}
amenities["Hungarian"] =  ("fuelstation", "library","motorway", "pubs", "supermarket")



