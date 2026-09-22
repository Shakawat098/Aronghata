import json
import pandas as pd

def generate_soil_profile(json_path='../data/aronghata_soil.json',csv_path='../data/aronghata_soil.csv'):
    soil_params={
        'site_name':'Aronghata_Khulna',
        'soil_series':'Ganges Tidal Alluvium (Non-saline)',
        'soil_texture':'Silty Clay Loam',
        'clay_fraction':0.34,
        'silt_fraction':0.48,
        'sand_fraction':0.18,
        'bulk_density_g_cm3':1.36,
        'soil_ph':6.9,
        'soil_organic_carbon_pct':0.95,
        'field_capacity':0.38,
        'wilting_capacity':0.18,
        'percolation_rate_mm_day':3.2,
        'bund_height_mm':80.0,
    }
    with open(json_path,'w',encoding='utf-8') as f:
        json.dump(soil_params,f,indent=4)
    
    df=pd.DataFrame([soil_params])
    df.to_csv(csv_path,index=False)
    print('file is ready')
    return soil_params

if __name__=='__main__':
    generate_soil_profile()
    