// ============================================================
// ROI PROVINSI KALIMANTAN BARAT
// Sumber batas administrasi: BIG 2026
// ============================================================
// Memanggil asset batas Provinsi Kalimantan Barat
var roi = ee.FeatureCollection(
  'projects/ratihdwifardilah/assets/Kalimantan_Barat_2026'
);

// Fokus peta ke wilayah kajian
Map.centerObject(roi, 7);

// Style ROI
var roiStyle = roi.style({
  color: '1565C0',        // garis batas biru
  fillColor: '1565C055',  // isi biru transparan
  width: 2
});

// Menampilkan ROI pada peta
Map.addLayer(
  roiStyle,
  {},
  'Provinsi Kalimantan Barat'
);

// Menampilkan informasi ROI di Console
print(
  'ROI Provinsi Kalimantan Barat:',
  roi
);

// ============================================================
// DATA RASTER INPUT 
// PROVINSI KALIMANTAN BARAT
// JULI-SEPTEMBER 2026
// ============================================================
var roi = ee.FeatureCollection(
  'projects/ratihdwifardilah/assets/Kalimantan_Barat_2026'
);

var start = '2026-07-01';
var end   = '2026-10-01';

Map.centerObject(roi, 7);

// ============================================================
// 1. SENTINEL-5P - AEROSOL INDEX
// ============================================================
var aerosol = ee.ImageCollection(
  'COPERNICUS/S5P/NRTI/L3_AER_AI'
)
.filterDate(start, end)
.filterBounds(roi)
.select('absorbing_aerosol_index')
.mean()
.clip(roi);

Map.addLayer(
  aerosol,
  {
    min: -1,
    max: 1,
    palette: [
      '313695',
      '4575b4',
      '74add1',
      'abd9e9',
      'e0f3f8',
      'ffffbf',
      'fee090',
      'fdae61',
      'f46d43',
      'd73027'
    ]
  },
  'Sentinel-5P Aerosol Index'
);

// ===========================================================
// 2. ERA5-LAND - TEMPERATURE 2 METER
// ============================================================
var temperature = ee.ImageCollection(
  'ECMWF/ERA5_LAND/DAILY_AGGR'
)
.filterDate(start, end)
.filterBounds(roi)
.select('temperature_2m')
.mean()
.subtract(273.15)
.clip(roi);

Map.addLayer(
  temperature,
  {
    min: 20,
    max: 35,
    palette: [
      '313695',
      '74add1',
      'ffffbf',
      'fdae61',
      'a50026'
    ]
  },
  'ERA5-Land Temperature 2m'
);

// ============================================================
// 3. WORLDPOP 2020
// ============================================================
var population = ee.ImageCollection(
  'WorldPop/GP/100m/pop'
)
.filter(
  ee.Filter.eq('country', 'IDN')
)
.filter(
  ee.Filter.eq('year', 2020)
)
.first()
.select('population')
.clip(roi);

Map.addLayer(
  population,
  {
    min: 0,
    max: 100,
    palette: [
      'ffffcc',
      'ffeda0',
      'feb24c',
      'f03b20',
      'bd0026'
    ]
  },
  'WorldPop 2020'
);

// ============================================================
// BATAS WILAYAH
// ============================================================
var boundary = roi.style({
  color: '000000',
  fillColor: '00000000',
  width: 2
});

Map.addLayer(
  boundary,
  {},
  'Batas Provinsi Kalimantan Barat'
);


