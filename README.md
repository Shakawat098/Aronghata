# Agro-Hydrological Modeling and Carbon Footprint Assessment of Boro Rice under Alternate Wetting and Drying (Safe-AWD) vs. Continuous Flooding

### A Case Study of Aronghata, Khulna

<p align="center">
  <img src="https://img.shields.io/badge/DSSAT-v4.8.6.000-blue?style=for-the-badge&logo=code" alt="DSSAT v4.8.6.000" />
  <img src="https://img.shields.io/badge/Model-CERES--Rice-green?style=for-the-badge" alt="CERES-Rice" />
  <img src="https://img.shields.io/badge/Method-FAO--56%20Penman--Monteith-orange?style=for-the-badge" alt="FAO-56 Penman-Monteith" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
</p>

---

**Author:** Md Shakawat Hossain[cite: 2]  
**Department:** Department of Farm Power and Machinery[cite: 2]  
**Faculty:** Faculty of Agricultural Engineering and Technology[cite: 2]  
**Institution:** Khulna Agricultural University, Khulna, Bangladesh[cite: 2]  
**Model Tools Used:** DSSAT v4.8.6.000 (CERES-Rice module) and the FAO-56 Penman-Monteith method[cite: 2]
**Date:** September 22, 2026

> **Note:** This is a practice project, not a field research study[cite: 2]. Most soil, crop-management and irrigation input values used in the model are empirical or assumed values taken from general references, not from laboratory tests or field measurements on this site[cite: 2]. The purpose was to practice building and running the modeling pipeline and to compare the two water-management methods[cite: 2]. This is explained in more detail in Section 2 and Section 6[cite: 2].

---

## Table of Contents

1. [Summary](#1-summary)
2. [Method](#2-method)
   - [2.1 Study Site and Geographic Coordinates](#21-study-site-and-geographic-coordinates)
   - [2.2 Weather data](#22-weather-data)
   - [2.3 Water use and irrigation schedule](#23-water-use-and-irrigation-schedule)
   - [2.4 Soil information](#24-soil-information)
   - [2.5 Crop and management setup](#25-crop-and-management-setup)
   - [2.6 Note on the methane (CH4) estimate](#26-note-on-the-methane-ch4-estimate)
3. [Results](#3-results)
4. [Discussion](#4-discussion)
   - [4.1 Where the water saving comes from](#41-where-the-water-saving-comes-from)
   - [4.2 Crop growth and yield](#42-crop-growth-and-yield)
   - [4.3 Estimated methane change](#43-estimated-methane-change)
5. [Figures](#5-figures)
6. [Data Sources and Assumptions](#6-data-sources-and-assumptions)

---

## 1. Summary

This project compares two water-management methods for Boro rice grown at Aronghata, Khulna, during the 2026 season: Continuous Flooding (CF), the common practice, and Safe Alternate Wetting and Drying (Safe-AWD), a water-saving method[cite: 2]. The comparison was done using a computer model (DSSAT, CERES-Rice module) together with the FAO-56 method for calculating water use, rather than a field trial[cite: 2].

The results from the model show that Safe-AWD used noticeably less irrigation water than continuous flooding, needed fewer irrigation events, and did not cause any water-stress penalty to the crop in the simulation[cite: 2]. Grain yield was almost the same under both methods[cite: 2].

- **Irrigation water used:** 639.9 mm under CF, compared to 516.5 mm under Safe-AWD — a saving of about 123.4 mm (around 19%)[cite: 2].
- **Number of irrigation events:** 19 under CF, compared to 8 under Safe-AWD — 11 fewer pumping events (about 58% fewer)[cite: 2].
- **Simulated water-stress index:** 0.000 (no stress) under both methods, at every growth stage[cite: 2].
- **Grain yield:** 287 kg/ha under CF and 279 kg/ha under Safe-AWD — a small difference of about 3%[cite: 2].

The yield values above are low compared with normal field yields[cite: 2]. This is because no nitrogen fertilizer was applied in either simulation (0 kg N/ha)[cite: 2]. This was done on purpose, so that the comparison would show only the effect of the water-management method, without fertilizer use affecting the result[cite: 2]. Because of this, the yield numbers should not be treated as an estimate of what a real, fertilized field would produce[cite: 2].

As explained in Section 2 and Section 6, the soil properties, crop-management dates, and irrigation amounts used in the model were not measured in the field or in a laboratory[cite: 2]. They are empirical (assumed) values taken from general references and from the model's own calculations, used to test and practice the modeling process[cite: 2].

---

## 2. Method

The work was done across structured steps: defining site geographic parameters, acquiring weather data, calculating water use and irrigation schedules, setting up soil and crop information, and running the DSSAT crop model for the two water-management methods[cite: 2].

### 2.1 Study Site and Geographic Coordinates

- **Location:** Aronghata, Khulna Sadar / Khan Jahan Ali Thana, Khulna District, South-Western Coastal Region, Bangladesh.
- **Geographic Coordinates:** Latitude: 22.864° N (22.88° N grid centroid), Longitude: 89.502° E (89.51° E grid centroid)[cite: 2].
- **Elevation:** ~4.0 m above mean sea level[cite: 2].
- **Agro-Ecological Zone:** AEZ 13 (Ganges Tidal Floodplain, Non-saline coastal alluvium zone)[cite: 2].

<p align="center">
  <img src="figures/Aronghata.png" alt="Satellite Imagery of Aronghata, Khulna Study Area" width="800"/>
</p>

_Figure: High-resolution satellite basemap showing the Aronghata, Khulna modeling site (22.864° N, 89.502° E) within the Ganges Tidal Floodplain (AEZ 13), Bangladesh._

### 2.2 Weather data

- Daily weather data (solar radiation, maximum and minimum temperature, rainfall, wind speed, and relative humidity) were downloaded from the NASA POWER database for the Aronghata, Khulna location (22.88° N, 89.51° E, elevation 4.0 m)[cite: 2].
- This data was arranged into the weather-file format DSSAT needs (file name `BDAR2601.WTH`)[cite: 2].
- Total rainfall over the 120-day crop period was 336.2 mm, the same for both simulations, since both used the same weather record[cite: 2].

### 2.3 Water use and irrigation schedule

- Daily crop water use (evapotranspiration) was calculated using the standard FAO-56 Penman-Monteith method, in Python[cite: 2].
- Crop coefficients were used at different growth stages to work out when the soil would need irrigation under each method[cite: 2].
- **Safe-AWD rule:** irrigate back up to 5 cm of standing water whenever the water table dropped to 15 cm below the soil surface, except during flowering, when the field was kept flooded[cite: 2].
- **Continuous Flooding (CF):** the field was kept flooded with a shallow water layer for the whole season, as is common practice[cite: 2].

#### FAO-56 Penman-Monteith Equation

Used to calculate reference evapotranspiration ($ET_o$)[cite: 2]:

$$ET_o = \frac{0.408 \Delta (R_n - G) + \gamma \left(\frac{900}{T + 273}\right) u_2 (e_s - e_a)}{\Delta + \gamma (1 + 0.34 u_2)}$$

Where:

- $R_n$ is net radiation[cite: 2]
- $G$ is soil heat flux[cite: 2]
- $T$ is mean daily air temperature[cite: 2]
- $u_2$ is wind speed at 2 m[cite: 2]
- $e_s - e_a$ is the vapour pressure deficit[cite: 2]
- $\Delta$ is the slope of the saturation vapour pressure curve[cite: 2]
- $\gamma$ is the psychrometric constant[cite: 2]

> **Note on irrigation dates:** The irrigation dates and water-table depths were first worked out separately using the FAO-56 daily water-balance calculation, assuming typical percolation behaviour for puddled coastal clay soil[cite: 2]. When this was carried over into the DSSAT soil-layer model, a standard drainage setting ($SLDR = 0.40$) was used to represent water movement through the 0–60 cm soil profile[cite: 2].

### 2.4 Soil information

> **Note:** The soil properties used in the model were not measured from a soil sample taken at this site[cite: 2]. They were assumed values, based on typical figures reported in the literature for Ganges tidal alluvium soil with a silty clay loam texture (DSSAT soil type code `SICL`, soil ID `BDAR000001`)[cite: 2]. This was done for practice and to test the modeling steps, not as a substitute for a real soil test[cite: 2].

- **Soil depth divided into layers:** 0–5, 5–15, 15–30, 30–45, and 45–60 cm[cite: 2].
- **Water-holding values (assumed):** wilting point 0.18–0.21 cm³/cm³; field capacity 0.38–0.40 cm³/cm³; saturation 0.46–0.48 cm³/cm³[cite: 2].
- **Bulk density (assumed):** 1.36–1.45 g/cm³[cite: 2].
- **Organic carbon (assumed):** about 0.95% near the surface, decreasing to 0.33% at depth[cite: 2].
- **Soil pH (assumed):** 6.9–7.2[cite: 2].
- **Hydraulic settings:** Runoff curve number: 75.0; Drainage rate: 0.40; Surface albedo: 0.13; Evaporation limit: 6.0 mm[cite: 2].

### 2.5 Crop and management setup

- **Crop:** rice (_Oryza sativa L._), variety BR 3 (Boro)[cite: 2]. DSSAT variety code `IB0027`[cite: 2]. The genetic growth parameters for this variety ($P_1, P_{2R}, P_5, P_{2O}, G_1, G_2, G_3$) were taken directly from DSSAT's built-in variety list; they were not adjusted or calibrated for this study[cite: 2].
- **Transplanting:** 30-day-old seedlings were transplanted on 15 January 2026; the crop reached maturity on 15 May 2026 (120 days after transplanting)[cite: 2]. Row spacing 20 cm; plant density 25 plants per m²[cite: 2].
- **Nutrient control:** No nitrogen fertilizer was applied in either simulation (0 kg N/ha), so that the comparison would reflect only the effect of the water-management method[cite: 2].

### 2.6 Note on the methane (CH4) estimate

> **Note:** Methane emissions were not measured in the field (for example, with gas-sampling chambers)[cite: 2]. The estimated 34% drop in methane under Safe-AWD is a calculated estimate only[cite: 2]. It comes from combining the daily water-table pattern from the FAO-56 water balance with standard IPCC Tier-2 emission factors for rice fields under different water regimes[cite: 2].

Under continuous flooding, the soil stays wet and low in oxygen for the whole season, which is the condition under which methane-producing microbes are most active (this corresponds to a Tier-2 scaling factor of 1.0)[cite: 2]. Under Safe-AWD, the field dries out periodically before being re-flooded, which lets oxygen back into the soil[cite: 2]. This slows down methane production and allows methane-consuming microbes to become more active, which is why the Tier-2 method gives a lower emission estimate for Safe-AWD[cite: 2].

Because this number comes from a calculation, not a field measurement, it should be described as an estimate of possible methane reduction, not as a measured result[cite: 2].

---

## 3. Results

Table 1 below shows the main results taken from the DSSAT output file (`OVERVIEW.OUT`) for the two simulations: Run 1 (Continuous Flooding) and Run 2 (Safe-AWD)[cite: 2].

### Table 1. Comparison of results between Continuous Flooding and Safe-AWD

| Measure                             |         CF         |  Safe-AWD   | Difference  | Comment                                     |
| :---------------------------------- | :----------------: | :---------: | :---------: | :------------------------------------------ |
| **Total irrigation applied**        |      639.9 mm      |  516.5 mm   |  −123.4 mm  | About 19% less water used[cite: 2]          |
| **Number of irrigation events**     |         19         |      8      |     −11     | About 58% fewer pumping events[cite: 2]     |
| **Seasonal rainfall**               |      336.2 mm      |  336.2 mm   |   0.0 mm    | Same weather data used for both[cite: 2]    |
| **Water-stress index**              |       0.000        |    0.000    |    0.000    | No stress simulated in either case[cite: 2] |
| **Evapotranspiration (total)**      |      414.8 mm      |  321.7 mm   |  −93.1 mm   | Mostly less soil evaporation[cite: 2]       |
| **Plant transpiration**             |      35.7 mm       |   36.7 mm   |   +1.0 mm   | Almost unchanged[cite: 2]                   |
| **Grain yield (dry weight)**        |     287 kg/ha      |  279 kg/ha  |  −8 kg/ha   | Small difference, about 3%[cite: 2]         |
| **Total crop biomass**              |    1,092 kg/ha     | 1,080 kg/ha |  −12 kg/ha  | Almost the same[cite: 2]                    |
| **Harvest index**                   |       0.263        |    0.258    |   −0.005    | Almost unchanged[cite: 2]                   |
| **Yield per m³ irrigation water**   |     0.04 kg/m³     | 0.05 kg/m³  | +0.01 kg/m³ | Better water-use efficiency[cite: 2]        |
| **Biomass per m³ irrigation water** |     0.17 kg/m³     | 0.21 kg/m³  | +0.04 kg/m³ | Better water-use efficiency[cite: 2]        |
| **Estimated methane change**        | Higher (reference) |    Lower    | About −34%  | Estimated, not measured (see 2.6)[cite: 2]  |

The water-use efficiency figures show that although Safe-AWD used less water overall, it produced slightly more grain and biomass for each cubic metre of irrigation water applied, compared with continuous flooding[cite: 2].

---

## 4. Discussion

### 4.1 Where the water saving comes from

The model output shows that almost all of the water saved under Safe-AWD comes from a reduction in soil and surface evaporation, not from a reduction in how much water the plant itself uses[cite: 2]. Season-total soil evaporation was about 379.7 mm under CF, compared to about 285.7 mm under Safe-AWD — a difference of roughly 94 mm[cite: 2]. Plant transpiration, on the other hand, stayed almost the same: about 35 mm under CF and about 36 mm under Safe-AWD[cite: 2].

This matters because it means the crop was not short of water at any point — the water saved was water that would otherwise have evaporated from the wet soil surface, not water the plant needed[cite: 2]. This is also why the water-stress index stayed at 0.000 for both methods throughout the season[cite: 2].

#### Figure A. Plant water use compared with soil evaporation

<p align="center">
  <img src="figures/Beneficial Transpiration vs. Non-Beneficial Evaporation.png" alt="Figure A - Plant water use compared with soil evaporation" width="750"/>
</p>

_Plant water use (blue) is almost the same for both methods (about 35 mm for CF and 36 mm for Safe-AWD)[cite: 2]. Soil evaporation (orange) drops noticeably, from about 380 mm under CF to about 286 mm under Safe-AWD[cite: 2]. This shows that the water saving under Safe-AWD mainly comes from less evaporation, not less water use by the plant[cite: 2]._

### 4.2 Crop growth and yield

The model shows that the crop reached each growth stage on the same day under both methods: panicle initiation at 54 days, flowering at 90 days, and maturity at 120 days after planting[cite: 2]. Maximum leaf area was also the same (0.13) in both cases[cite: 2]. This shows that the Safe-AWD water schedule did not delay or speed up crop development compared with continuous flooding[cite: 2].

As mentioned earlier, the low yield values (287 and 279 kg/ha) are a result of the zero-fertilizer setting used in both simulations, not a result of the water-management method[cite: 2]. This setting was chosen on purpose so that the water-management comparison would not be affected by differences in nitrogen supply[cite: 2]. With normal fertilizer use, yields under both methods would be expected to be much higher, although the general pattern of the comparison between CF and Safe-AWD would likely stay similar[cite: 2].

### 4.3 Estimated methane change

Continuous flooding keeps the soil wet and low in oxygen for the whole season[cite: 2]. This is the condition in which methane-producing microbes in the soil are most active[cite: 2]. Safe-AWD lets the field dry out periodically before re-flooding, which brings oxygen back into the topsoil[cite: 2]. This slows down methane production during the dry period and allows methane-consuming microbes to become more active[cite: 2]. Based on these water-table patterns and standard emission factors, the estimated methane reduction under Safe-AWD is about 34%[cite: 2].

As noted in Section 2.6, this is a calculated estimate based on water-table data and standard emission factors, not a value measured from gas samples taken in the field[cite: 2].

---

## 5. Figures

The figures below are taken from the DSSAT simulation output files (`ET.OUT`, `PlantGro.OUT` and `SoilWat.OUT`) for the two water-management methods[cite: 2].

#### Figure 1. Evapotranspiration and transpiration over time

<p align="center">
  <img src="figures/evapotranspiration.png" alt="Figure 1 - Evapotranspiration and transpiration over time" width="750"/>
</p>

_Cumulative evapotranspiration, soil evaporation, and transpiration (×10) over the growing season, for Continuous Flooding and Safe-AWD[cite: 2]. From around day 40 onward, the evapotranspiration lines for the two methods start to separate, mainly because of lower soil evaporation under Safe-AWD, while the transpiration lines for both methods stay close together[cite: 2]._

#### Figure 2. Crop biomass and grain weight over time

<p align="center">
  <img src="figures/plant_growth.png" alt="Figure 2 - Crop biomass and grain weight over time" width="750"/>
</p>

_Total biomass and grain weight for both methods over 120 days after planting[cite: 2]. The two biomass curves are very close to each other for most of the season, with only a small difference appearing after grain filling starts (around day 97), matching the near-equal biomass values at harvest (1,092 vs. 1,080 kg/ha)[cite: 2]._

#### Figure 3. Soil water and irrigation amounts over time

<p align="center">
  <img src="figures/soilwater.png" alt="Figure 3 - Soil water and irrigation amounts over time" width="750"/>
</p>

_Step-shaped lines show how irrigation water was added over time[cite: 2]. Continuous Flooding (pink line) received frequent, smaller amounts of water, reaching a total of 639.9 mm[cite: 2]. Safe-AWD (blue line) received fewer, larger amounts, reaching a total of 516.5 mm[cite: 2]. Total soil water (upper flat lines) stayed at a similar, stable level under both methods, showing that the root zone did not run short of water under Safe-AWD[cite: 2]._

---

## 6. Data Sources and Assumptions

This section lists, in one place, all the input values used in the model that were not measured in the field or laboratory for this study, so that it is clear which parts of the model are based on assumptions[cite: 2]. This is a class/practice project[cite: 2]. The main aim was to build and test the modeling steps and to compare irrigation water use between continuous flooding and Safe-AWD, not to produce a field-verified yield forecast[cite: 2].

### Table 2. Input values used without direct field or laboratory measurement

| Item                                                                      | Value used                                          | Source                                                                  |
| :------------------------------------------------------------------------ | :-------------------------------------------------- | :---------------------------------------------------------------------- |
| **Soil water limits (wilting point / field capacity / saturation)**       | 0.18–0.21 / 0.38–0.40 / 0.46–0.48 cm³/cm³           | Assumed, from general reference values for this soil type[cite: 2]      |
| **Soil bulk density**                                                     | 1.36–1.45 g/cm³                                     | Assumed[cite: 2]                                                        |
| **Soil organic carbon**                                                   | 0.95% (top) to 0.33% (deep)                         | Assumed general value[cite: 2]                                          |
| **Initial soil nitrogen (NO3 / NH4)**                                     | 0.0 kg/ha / 0.0 kg/ha                               | Not measured; assumed[cite: 2]                                          |
| **Drainage rate / runoff curve number**                                   | 0.40 / 75.0                                         | Assumed[cite: 2]                                                        |
| **Planting date**                                                         | 15 January 2026                                     | Assumed typical Boro planting date[cite: 2]                             |
| **Seedling age at transplanting**                                         | 30 days                                             | Assumed typical practice[cite: 2]                                       |
| **Plant density / row spacing**                                           | 25 plants/m² / 20 cm                                | Assumed typical spacing[cite: 2]                                        |
| **Planting depth**                                                        | 3 cm                                                | Assumed[cite: 2]                                                        |
| **Fertilizer applied**                                                    | 0 kg N/ha                                           | Set to zero on purpose, to isolate the water-method comparison[cite: 2] |
| **CF irrigation total / events**                                          | 640.0 mm / 19                                       | Calculated from the FAO-56 water balance[cite: 2]                       |
| **Safe-AWD irrigation total / events**                                    | 516.4 mm / 8                                        | Calculated from the FAO-56 water balance[cite: 2]                       |
| **Safe-AWD irrigation trigger**                                           | Re-flood at −15 cm water table, up to +5 cm         | Assumed, based on standard Safe-AWD guidance[cite: 2]                   |
| **Variety growth parameters ($P_1, P_{2R}, P_5, P_{2O}, G_1, G_2, G_3$)** | DSSAT default values for BR 3 (Boro), code `IB0027` | Taken from DSSAT's built-in variety database, not calibrated[cite: 2]   |

The soil, crop-management and fertilizer values used in this project are assumed or empirical values, used to test the modeling pipeline[cite: 2]. The variety growth parameters were used as they come from the DSSAT database, without adjustment[cite: 2]. The methane figure is a calculated estimate based on water-table data and standard emission factors, not a measured value[cite: 2].
