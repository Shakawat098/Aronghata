import pandas as pd
df=pd.read_csv('../data/aronghata_weather.csv')
df['Date']=pd.to_datetime(df['Date'])

df.insert(0, "Year", df["Date"].dt.year)
df.insert(1, "DOY", df["Date"].dt.dayofyear)

df = df.drop(columns=["Date"])

df.to_csv("../data/aronghata_weather_wm.csv", index=False)
print('Weatherman file is ready')