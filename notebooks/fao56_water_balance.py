import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_data(weather_csv='../data/aronghata_weather.csv',soil_json='../data/aronghata_soil.json'):
    df=pd.read_csv(
        weather_csv,index_col='Date',parse_dates=True
    )
    with open(soil_json,'r',encoding='utf-8') as f:
        soil=json.load(f)
    return df,soil

def calculate_fao56_et0(df,elevation=3.5):
    Tmean=(df['Tmax'] +df['Tmin'])/2.0
    P = 101.3 * (((293.0 - 0.0065 * elevation) / 293.0) ** 5.26)
    gamma = 0.000665 * P

    delta = (4098 * (0.6108 * np.exp((17.27 * Tmean) / (Tmean + 237.3)))) / (
        (Tmean + 237.3) ** 2
    )

    e_Tmax = 0.6108 * np.exp((17.27 * df["Tmax"]) / (df["Tmax"] + 237.3))
    e_Tmin = 0.6108 * np.exp((17.27 * df["Tmin"]) / (df["Tmin"] + 237.3))
    es = (e_Tmax + e_Tmin) / 2.0
    ea = es * (df["RH"] / 100.0)

    Rns = (1 - 0.23) * df["SolarRad_MJ"]  #albedo=0.23

    sigma = 4.903e-9
    Tmax_k4 = (df["Tmax"] + 273.16) ** 4
    Tmin_k4 = (df["Tmin"] + 273.16) ** 4
    Rnl = (
        sigma
        * ((Tmax_k4 + Tmin_k4) / 2.0)
        * (0.34 - 0.14 * np.sqrt(np.maximum(ea, 0)))
        * 0.8
    )

    Rn = Rns - Rnl
    G = 0

    u2 = df["WindSpeed_2m"]
    num = 0.408 * delta * (Rn - G) + gamma * (900 / (Tmean + 273)) * u2 * (
        es - ea
    )
    den = delta + gamma * (1 + 0.34 * u2)
    return np.maximum(num/den,0.5)


def get_rice_kc(dat):
    if dat<=20:
        return 1.05
    elif dat <= 50:
        return 1.05 + (1.20-1.05) * ((dat-20)/30.0)
    elif dat <= 90:
        return 1.20
    else:
        return 1.20-(1.20-0.70) * ((dat-90)/30.0)

def run_water_balance(weather_df,soil_params):
    df=weather_df.copy()
    df['ET0']=calculate_fao56_et0(df)
    days=len(df)
    df['Kc']=[get_rice_kc(i+1) for i in range(days)]
    df['ETc']=df['ET0'] * df['Kc']
    percolation=soil_params['percolation_rate_mm_day']
    bund_height=soil_params['bund_height_mm']
    
    wl_cf,wl_awd=50.0,50.0
    water_level_cf,water_level_awd=np.zeros(days),np.zeros(days)
    irr_cf,irr_awd=np.zeros(days),np.zeros(days)
    
    for i in range(days):
        rain=df['Rainfall_mm'].iloc[i]
        etc=df['ETc'].iloc[i]
        dat=i+1
        wl_cf=wl_cf +rain -etc-percolation
        if wl_cf<20.0:
            irr_cf[i]=50.0-wl_cf
            wl_cf=50.0
        wl_cf=min(wl_cf,bund_height)
            
        wl_awd=wl_awd + rain - etc - percolation
        is_sensitive=(dat <= 15) or (55<=dat <= 80)
            
        if is_sensitive:
            if wl_awd < 20.0:
                irr_awd[i]=50.0-wl_awd
                wl_awd=50.0
        else:
            if wl_awd <= -150.0:
                irr_awd[i]=50.0-wl_awd
                wl_awd=50.0
        wl_awd = min(wl_awd,bund_height)
        water_level_awd[i]=wl_awd
        
    df['WL_CF_mm']=water_level_cf
    df['WL_AWD_mm']=water_level_awd
    df['Irrigation_CF_mm']=irr_cf
    df['Irrigation_AWD_mm']=irr_awd
    return df

if __name__ == '__main__':
    weather_df,soil_params=load_data()
    
    results=run_water_balance(weather_df,soil_params)
    results.to_csv('../data/aronghata_water_balance.csv')
    
    cf_tot=results['Irrigation_CF_mm'].sum()
    awd_tot=results['Irrigation_AWD_mm'].sum()
    saving=((cf_tot-awd_tot)/cf_tot)*100
    
    print('Results')
    print(f'cf total irrigation {cf_tot:.1f} mm results----- ({(results['Irrigation_CF_mm']>0).sum()})')
    print(f'AWD total irrigation {awd_tot:.1f} mm results--- ({(results['Irrigation_AWD_mm']>0).sum()})')
    print(f'water saved:{saving:.2f}%')
    
    plt.figure(figsize=(12, 5))
    plt.plot(
        results.index,
        results["WL_CF_mm"],
        label="Continuous Flooding (CF)",
        color="royalblue",
        linewidth=1.5,
    )
    plt.plot(
        results.index,
        results["WL_AWD_mm"],
        label="Safe-AWD",
        color="forestgreen",
        linewidth=1.8,
    )
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8, label="Soil Surface")
    plt.axhline(
        -150,
        color="crimson",
        linestyle=":",
        linewidth=1.2,
        label="AWD Threshold (-150 mm)",
    )

    plt.title(
        "Paddy Field Water Dynamics: Arongghata, Khulna (Boro Season)",
        fontsize=12,
        fontweight="bold",
    )
    plt.xlabel("Date", fontsize=10)
    plt.ylabel("Water Table / Ponding Depth (mm)", fontsize=10)
    plt.legend(loc="lower left")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig('ContinousFlooding-AwdPlot.png',dpi=300,bbox_inches='tight')
    plt.show()