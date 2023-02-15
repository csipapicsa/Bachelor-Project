import main as m

def NetCDFtoGeoPandas(PATH):
    DS = m.xr.open_dataset(PATH)

    # write to csv
    # DS.to_dataframe().to_csv("output_filename.csv")
    # read in
    df = DS.to_dataframe()
    df = m.gpd.GeoDataFrame(
        df, geometry=m.gpd.points_from_xy(df.lon, df.lat))

    # convert values
    df["lon"] = df["lon"].astype(float)
    df["lat"] = df["lat"].astype(float)
    # double conversation needs
    df.CO = df.CO.astype(float).astype(int)
    # important! 
    df.crs = "EPSG:23700" #Hungary
    #print(df.head())
    # filter, since there are duplications
    df = df[df["Times_bnds"] == min(df["Times_bnds"])]
    ###########################################
    ###########################################
    # filter focusing on Hungary
    df = df[df["lon"] < 23.02]
    df = df[df["lon"] > 16.072]
    df = df[df["lat"] > 45.699]
    df = df[df["lat"] < 48.7]
    
    #drop index and unused columns
    df.reset_index(drop=True, inplace=True)
    df.drop(['Times_bnds'], axis=1, inplace=True)
    #df.drop(['Times', 'bnds','south_north','est_east','Times_bnds'], axis=1)

    # since there are only points, expand them to square
    for key in df.index:
        df.geometry[key] = m.Polygon(((df.lon[key]-0.1, df.lat[key]),
                    (df.lon[key], df.lat[key]),
                   (df.lon[key], df.lat[key]+0.1),

                   (df.lon[key]-0.1, df.lat[key]+0.1)))
    
    return df
    
def AverageAirQuality(FOCUS, FILES):
    dfCounter = 0
    l = len(FILES)
    valueLists = []
    for i in range(l):
        df = NetCDFtoGeoPandas(PATH["weather"]+FILES[i])
        if dfCounter == 0:
            dfFinal = df
            valueLists.append(df[FOCUS])
            dfFinal.rename(columns={FOCUS: str(FOCUS+"-"+str(i))}, inplace=True)
        else:
            valueLists.append(df[FOCUS])
            dfFinal[str(FOCUS+"-"+str(i))] = df[FOCUS]
            #df.rename(columns={FOCUS: str(FOCUS+"-"+str((i+1)))}, inplace=True)
        dfCounter += 1

    # Later on:
    valueLists = np.column_stack(valueLists)
    # max
    dfFinal[str(FOCUS+"-max")] = np.amax(valueLists, axis=1) #max value
    dfFinal[str(FOCUS+"-avg")] = np.rint(np.average(valueLists, axis=1)) # average and integer
    dfFinal.crs = "epsg:4326"
    
    # drop unused columns
    for i in range(l):
        dfFinal.drop(columns={str(FOCUS+"-"+str(i))}, inplace=True)
    return dfFinal    
 