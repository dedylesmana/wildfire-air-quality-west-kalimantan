# West Kalimantan PM2.5 Estimation and Wildfire Air Quality Analysis

Remote sensing-based spatial estimation of PM2.5 and population exposure assessment over West Kalimantan, Indonesia.

## Project Overview

This project develops a remote sensing-based workflow for spatial estimation of PM2.5 over West Kalimantan, Indonesia.

The analysis integrates satellite observations, meteorological variables, population data, Google Earth Engine, Python, and Random Forest modelling to investigate the spatial distribution of estimated PM2.5 during July–September 2026.

The project focuses on spatial assessment of PM2.5 conditions during periods associated with wildfire and biomass-burning activity.

## Study Area

The study area covers West Kalimantan Province, Indonesia.

Administrative boundaries from BIG are used as the geographic reference for the spatial analysis.

## Data Sources

The project integrates the following datasets:

- Sentinel-5P atmospheric observations
- ERA5-Land meteorological variables
- WorldPop 2020 population data
- BIG administrative boundaries
- Model-derived PM2.5 spatial data

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

WorldPop 2020 data are used to support population exposure assessment.

### Administrative Boundaries

Administrative boundaries from BIG are used to define the West Kalimantan study area.

## Analysis Period

The atmospheric analysis covers:

**July–September 2026**

Population exposure assessment uses WorldPop 2020 data.

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
9. Determine relatively high PM2.5 areas using the 75th percentile threshold.
10. Integrate PM2.5 estimates with WorldPop population data.
11. Estimate population exposure within relatively high PM2.5 zones.
12. Visualize the results through maps, figures, and an interactive Streamlit dashboard.

## Machine Learning Model

The project uses **Random Forest regression** to estimate PM2.5 from atmospheric and meteorological predictors.

Model performance is evaluated using:

- R2
- RMSE

Current model evaluation results:

| Metric | Value |
|---|---:|
| R2 | 0.948 |
| RMSE | 3.356 |

The reported model evaluation represents the relationship between the simulated PM2.5 target and Random Forest predictions.

## Spatial PM2.5 Estimation

The trained Random Forest model is applied to spatial predictor data to generate PM2.5 estimates across West Kalimantan.

The main spatial dataset is:

```text
data/pm25_spatial_kalbar.csv

## Project Purpose

This project provides a reproducible framework for integrating:

**Satellite observations + meteorological data + machine learning + population data + geospatial analysis**

for spatial assessment of PM2.5 during wildfire-related air pollution periods.

The workflow can support further research and development toward spatial air quality assessment and early warning applications.

## Author

**M. Dedy Lesmana**

West Kalimantan PM2.5 and Wildfire Air Quality Analysis

Indonesia

## License

This project is provided for research and academic purposes.

Further licensing information can be added as the project develops.