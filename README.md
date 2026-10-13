# West Kalimantan PM2.5 Estimation and Wildfire Air Quality Analysis

Remote sensing-based spatial estimation of PM2.5 and population exposure assessment over West Kalimantan, Indonesia.

This research project integrates satellite observations, meteorological variables, population data, Google Earth Engine, Python, and Random Forest modelling to investigate the spatial distribution of estimated PM2.5 during July-September 2026.

---

## Project Overview

Forest and land fires can contribute to elevated atmospheric pollution, particularly fine particulate matter (PM2.5).

This project develops a remote sensing-based spatial estimation workflow for PM2.5 over West Kalimantan, Indonesia.

The workflow integrates satellite-derived atmospheric indicators, meteorological variables, population data, geospatial processing, and machine learning to produce spatial estimates of PM2.5 and assess population exposure in areas with relatively high estimated concentrations.

The project also provides an interactive Streamlit dashboard for visualizing the analysis results.

---

## Study Area

The study area covers West Kalimantan Province, Indonesia.

Administrative boundaries from the Geospatial Information Agency of Indonesia (BIG) are used as the geographic reference for the spatial analysis.

---

## Data Sources

The analysis integrates the following datasets:

- Sentinel-5P atmospheric observations
- ERA5-Land meteorological variables
- WorldPop 2020 population data
- Administrative boundaries from BIG
- Model-derived PM2.5 spatial data
- Wildfire and biomass-burning related spatial information

### Sentinel-5P

Satellite-derived atmospheric indicators are used as spatial predictors, including:

- Aerosol Index
- NO2
- HCHO

### ERA5-Land

Meteorological variables include:

- 2 m air temperature
- Wind components

### WorldPop

WorldPop 2020 population data are used to support population exposure assessment.

### Administrative Boundaries

Administrative boundaries from BIG are used to define the West Kalimantan study area.

---

## Analysis Period

The atmospheric analysis covers:

**July-September 2026**

Population exposure assessment uses WorldPop 2020 data.

---

## Methodology

The analysis follows a multi-stage geospatial and machine learning workflow:

1. Define the West Kalimantan study area.
2. Prepare satellite-derived atmospheric indicators using Google Earth Engine.
3. Extract meteorological variables from ERA5-Land.
4. Integrate atmospheric and meteorological predictors.
5. Develop a Random Forest regression model for PM2.5 estimation.
6. Evaluate model performance using R2 and RMSE.
7. Apply the trained model to spatial predictor data.
8. Generate a spatial PM2.5 estimation map.
9. Identify relatively high PM2.5 areas using the 75th percentile threshold.
10. Integrate PM2.5 estimates with WorldPop population data.
11. Estimate population exposure within relatively high PM2.5 zones.
12. Visualize the results through maps, figures, and an interactive Streamlit dashboard.

---

## Machine Learning Model

The project uses **Random Forest regression** to estimate PM2.5 from atmospheric and meteorological predictors.

Model performance is evaluated using:

- R2
- RMSE

### Model Performance

| Metric | Value |
|---|---:|
| R2 | 0.948 |
| RMSE | 3.356 |

The reported model evaluation represents the relationship between the simulated PM2.5 target and Random Forest predictions.

---

## Spatial PM2.5 Estimation

The trained Random Forest model is applied to spatial predictor data to generate PM2.5 estimates across West Kalimantan.

The resulting spatial dataset is stored in:

```text
data/pm25_spatial_kalbar.csv

---

## Population Exposure Assessment

Population exposure assessment combines the spatial PM2.5 estimation with WorldPop 2020 population data.

Areas with relatively high PM2.5 concentrations are identified using the 75th percentile threshold.

The resulting analysis provides an estimate of population exposure within areas characterized by relatively high estimated PM2.5 concentrations.

### Population Exposure

![Population Exposure](figures/paparan_populasi_kalbar.png)

---

## Atmospheric Parameters

Sentinel-5P atmospheric indicators are incorporated into the spatial modelling workflow.

The atmospheric parameters used in the analysis include:

- Aerosol Index
- NO2
- HCHO

### Sentinel-5P Atmospheric Parameters

![Sentinel-5P Atmospheric Parameters](figures/parameter_atmosfer_s5p_kalbar.png)

---

## Model Performance Visualization

The model evaluation results are provided as a graphical visualization.

![Model Performance](figures/model_performance_kalbar.png)

---

## Interactive Dashboard

The project includes an interactive Streamlit dashboard for exploring the PM2.5 estimation results.

The dashboard provides visualization of:

- Spatial PM2.5 estimation
- Model performance
- Atmospheric parameters
- Population exposure
- Study area information

The dashboard application is implemented in:

```text
app.py
---

## Google Earth Engine

Google Earth Engine is used for geospatial data preparation and satellite-based atmospheric data processing.

The Earth Engine workflow is stored in:

```text
gee/Kalbar_PM25_RasterInput.js
```

## Repository Structure

```text
wildfire-air-quality-west-kalimantan/
│
├── data/
│   ├── model_performance_kalbar.csv
│   ├── pm25_spatial_kalbar.csv
│   └── pm25_summary_kalbar.csv
│
├── figures/
│   ├── model_performance_kalbar.png
│   ├── paparan_populasi_kalbar.png
│   ├── parameter_atmosfer_s5p_kalbar.png
│   └── peta_pm25_kalbar.png
│
├── gee/
│   └── Kalbar_PM25_RasterInput.js
│
├── notebooks/
│   └── Estimasi_PM25_Karhutla_Kalimantan_Barat.ipynb
│
├── outputs/
│
├── scripts/
│
├── app.py
├── README.md
└── requirements.txt

---

## Installation

Clone the repository:

```bash
git clone https://github.com/dedylesmana/wildfire-air-quality-west-kalimantan.git
cd wildfire-air-quality-west-kalimantan
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the interactive dashboard:

```bash
streamlit run app.py
```

The application can then be accessed through the local Streamlit server.

---

## Research Outputs

The main outputs of this project include:

- Spatial PM2.5 estimation over West Kalimantan
- Random Forest model evaluation
- Sentinel-5P atmospheric parameter analysis
- Identification of relatively high PM2.5 areas
- Population exposure assessment
- Interactive PM2.5 visualization dashboard

### PM2.5 Spatial Estimation

![PM2.5 Spatial Estimation](figures/peta_pm25_kalbar.png)

### Model Performance

![Model Performance](figures/model_performance_kalbar.png)

### Population Exposure

![Population Exposure](figures/paparan_populasi_kalbar.png)

### Sentinel-5P Atmospheric Parameters

![Atmospheric Parameters](figures/parameter_atmosfer_s5p_kalbar.png)

---

## Google Earth Engine

Google Earth Engine is used for geospatial data preparation and satellite-based atmospheric data processing.

The Earth Engine workflow is stored in:

```text
gee/Kalbar_PM25_RasterInput.js
```

This script supports the preparation of spatial predictor data used in the PM2.5 estimation workflow.

---

## Interactive Dashboard

The project includes an interactive Streamlit dashboard for exploring the PM2.5 estimation results.

The dashboard provides visualization of:

- Spatial PM2.5 estimation
- Model performance
- Atmospheric parameters
- Population exposure
- Study area information

The dashboard application is implemented in:

```text
app.py
```

To run the dashboard locally:

```bash
streamlit run app.py
```

---

## Research Context

This project is part of a broader research workflow on wildfire, atmospheric pollution, remote sensing, geospatial analysis, and machine learning.

The workflow is designed to support spatial assessment of PM2.5 conditions associated with wildfire and biomass-burning activity in West Kalimantan.

The results can support further research on air quality monitoring, wildfire impact assessment, spatial exposure analysis, and environmental decision support.

---

## Author

**M. Dedy Lesmana**

West Kalimantan PM2.5 and Wildfire Air Quality Analysis

Indonesia

---

## License

This project is provided for research and academic purposes.

Please contact the author before using the project for commercial purposes or redistributing modified versions.