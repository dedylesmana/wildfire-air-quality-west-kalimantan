
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# DASHBOARD ESTIMASI PM2.5 KALIMANTAN BARAT
# ============================================================
st.set_page_config(
    page_title="Dashboard Estimasi PM2.5 Provinsi Kalimantan Barat",
    layout="wide"
)

st.title("Dashboard Estimasi PM2.5 Provinsi Kalimantan Barat")
st.caption("Periode analisis: Juli–September 2026")
st.markdown("---")

# ============================================================
# MEMBACA DATA HASIL ANALISIS
# ============================================================
data = pd.read_csv(
    "data/pm25_spatial_kalbar.csv"
)

summary = pd.read_csv(
    "data/pm25_summary_kalbar.csv"
)

performance = pd.read_csv(
    "data/model_performance_kalbar.csv"
)

summary_dict = dict(
    zip(
        summary["Parameter"],
        summary["Value"]
    )
)

rmse = float(summary_dict["RMSE"])
r2 = float(summary_dict["R2"])
threshold = float(summary_dict["Threshold_Q75"])

total_population = float(
    summary_dict["Total_Population"]
)

high_population = float(
    summary_dict["High_PM25_Population"]
)

exposure_percent = float(
    summary_dict["Exposure_Percent"]
)

# ============================================================
# PETA PM2.5 DAN RINGKASAN MODEL
# ============================================================
col1, col2 = st.columns([7, 3])

with col1:

    st.subheader(
        "Distribusi Spasial Estimasi PM2.5"
    )

    fig_map, ax_map = plt.subplots(
        figsize=(10, 7)
    )

    pm25_plot = ax_map.scatter(
        data["longitude"],
        data["latitude"],
        c=data["PM25_Map"],
        cmap="turbo",
        marker="s",
        s=20,
        linewidths=0
    )

    high_data = data[
        data["PM25_Map"] >= threshold
    ]

    ax_map.scatter(
        high_data["longitude"],
        high_data["latitude"],
        facecolors="none",
        edgecolors="black",
        marker="s",
        s=24,
        linewidths=0.35,
        label="Zona relatif tinggi (Q75)"
    )

    cbar = fig_map.colorbar(
        pm25_plot,
        ax=ax_map,
        shrink=0.82
    )

    cbar.set_label(
        "Estimasi PM2.5 Model"
    )

    ax_map.set_title(
        "Distribusi Spasial Estimasi PM2.5\n"
        "Provinsi Kalimantan Barat"
    )

    ax_map.set_xlabel("Longitude")
    ax_map.set_ylabel("Latitude")

    ax_map.legend(
        loc="lower left",
        fontsize=8
    )

    ax_map.grid(
        alpha=0.20,
        linestyle="--"
    )

    ax_map.set_aspect(
        "equal",
        adjustable="box"
    )

    plt.tight_layout()

    st.pyplot(fig_map)


with col2:

    st.subheader("Ringkasan Model")

    st.write(
        f"**RMSE:** {rmse:.3f}"
    )

    st.write(
        f"**R²:** {r2:.3f}"
    )

    st.write(
        f"**Threshold Q75:** {threshold:.3f}"
    )

    st.markdown("---")

    st.subheader(
        "Estimasi Paparan Populasi"
    )

    st.write(
        f"**Total populasi WorldPop:** "
        f"{total_population:,.0f} jiwa"
    )

    st.write(
        f"**Populasi zona PM2.5 relatif tinggi:** "
        f"{high_population:,.0f} jiwa"
    )

    st.write(
        f"**Persentase estimasi paparan:** "
        f"{exposure_percent:.2f}%"
    )

    fig_pop, ax_pop = plt.subplots(
        figsize=(5, 4)
    )

    kategori = [
        "Total\nPopulasi",
        "Zona PM2.5\nRelatif Tinggi"
    ]

    nilai = [
        total_population,
        high_population
    ]

    bars = ax_pop.bar(
        kategori,
        nilai
    )

    ax_pop.set_ylabel(
        "Jumlah Penduduk"
    )

    ax_pop.set_title(
        "Estimasi Paparan Populasi"
    )

    ax_pop.ticklabel_format(
        style="plain",
        axis="y"
    )

    for bar in bars:

        value = bar.get_height()

        ax_pop.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:,.0f}",
            ha="center",
            va="bottom",
            fontsize=8
        )

    plt.tight_layout()

    st.pyplot(fig_pop)

# ============================================================
# MODEL PERFORMANCE
# ============================================================
st.markdown("---")

st.subheader(
    "Kinerja Model Random Forest"
)

fig_perf, ax_perf = plt.subplots(
    figsize=(8, 6)
)

ax_perf.scatter(
    performance["Target_PM25_Simulasi"],
    performance["Prediksi_PM25"],
    alpha=0.65
)

min_value = min(
    performance["Target_PM25_Simulasi"].min(),
    performance["Prediksi_PM25"].min()
)

max_value = max(
    performance["Target_PM25_Simulasi"].max(),
    performance["Prediksi_PM25"].max()
)

ax_perf.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--",
    label="Prediksi ideal"
)

ax_perf.set_xlabel(
    "Target PM2.5 Simulasi"
)

ax_perf.set_ylabel(
    "Prediksi PM2.5 Random Forest"
)

ax_perf.set_title(
    f"Target PM2.5 Simulasi vs Prediksi Model\n"
    f"R² = {r2:.3f} | RMSE = {rmse:.3f}"
)

ax_perf.grid(
    alpha=0.25,
    linestyle="--"
)

ax_perf.legend()

plt.tight_layout()

st.pyplot(fig_perf)

st.caption(
    "Grafik membandingkan target PM2.5 simulasi pada data uji "
    "dengan hasil prediksi Random Forest. Evaluasi ini bukan "
    "validasi terhadap pengukuran PM2.5 stasiun lapangan."
)

# ============================================================
# Estimasi PAPARAN SPASIAL
# ============================================================
st.markdown("---")

st.subheader(
    "Estimasi Paparan Spasial"
)

st.write(
    f"Sebanyak **{exposure_percent:.2f}%** populasi WorldPop "
    f"atau sekitar **{high_population:,.0f} jiwa** berada pada "
    "zona estimasi PM2.5 relatif tinggi."
)

st.caption(
    f"Zona relatif tinggi ditentukan menggunakan threshold Q75 "
    f"sebesar {threshold:.3f}. Nilai ini merupakan klasifikasi "
    "relatif hasil model, bukan ambang baku kesehatan."
)

# ============================================================
# INTERPRETASI SPASIAL
# ============================================================
st.markdown("---")

st.subheader(
    "Interpretasi Spasial"
)

st.write(
    "Hasil model menunjukkan adanya variasi spasial estimasi "
    "PM2.5 di Kalimantan Barat. Nilai relatif tinggi cenderung "
    "terkonsentrasi pada bagian barat hingga barat daya wilayah "
    "kajian, sedangkan bagian timur dan timur laut menunjukkan "
    "nilai yang relatif lebih rendah."
)

# ============================================================
# INFORMASI DATASET
# ============================================================
st.markdown("---")

st.subheader(
    "Informasi Dataset"
)

st.write(
    "**Sentinel-5P:** Aerosol Index, NO₂, dan HCHO"
)

st.write(
    "**ERA5-Land:** Temperatur 2 meter dan komponen angin"
)

st.write(
    "**WorldPop 2020:** Distribusi populasi"
)

st.write(
    "**BIG 2026:** Batas administrasi Kalimantan Barat"
)

st.write(
    "**Periode data atmosfer:** Juli–September 2026"
)

# ============================================================
# CATATAN
# ============================================================
st.markdown("---")

st.caption(
    "Sumber data: Sentinel-5P, ERA5-Land, WorldPop 2020, "
    "dan batas administrasi BIG. PM2.5 merupakan estimasi "
    "model berbasis target simulasi."
)
