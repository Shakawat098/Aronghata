import pandas as pd
import requests
import numpy as np
import os

def fetch_nasa_data(lat,lon,start_date,end_date,output_path):
    url='https://power.larc.nasa.gov/api/temporal/daily/point'
    parameters=[
        'T2M_MAX',
        'T2M_MIN',
        'RH2M',
        'WS2M',
        'ALLSKY_SFC_SW_DWN',
        'PRECTOTCORR',
    ]
    params={
        'parameters':','.join(parameters),
        'community':'AG',
        'longitude':lon,
        'latitude':lat,
        'start': start_date,
        'end':end_date,
        'format':'JSON'
    }
    
    response=requests.get(url,params=params,timeout=30)
    response.raise_for_status()
    data=response.json()['properties']['parameter']
    df=pd.DataFrame(data)
    df.index=pd.to_datetime(df.index,format='%Y%m%d')
    df.index.name='Date'
    
    df=df.rename(
        columns={
            'T2M_MAX':'Tmax',
            'T2M_MIN':'Tmin',
            'RH2M':'RH',
            'WS2M':'WindSpeed_2m',
            'ALLSKY_SFC_SW_DWN':'SolarRad_MJ',
            'PRECTOTCORR':'Rainfall_mm',
        }
    )
    df=df.replace(-999.0,np.nan).ffill().bfill()
    
    df.to_csv(output_path)
    return df

aronghata_weather_df=fetch_nasa_data(lat=22.864,lon=89.502,start_date='20260115',end_date='20260515',output_path='../data/aronghata_weather.csv')
print('Aronghata weather data(first 5 days):')
print(aronghata_weather_df.head(-5))
