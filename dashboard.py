import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from load_data import load_data
from analyze import plot_data
from anomaly import detect_anomaly

st.title("AI Machine Data Analyzer Dashboard")

# 載入資料
df = load_data("data/sample_data.csv")

st.subheader("Raw Data")
st.dataframe(df)

# 異常偵測
anomalies = detect_anomaly(df)
st.subheader("Detected Anomalies")
st.dataframe(anomalies)

# 畫圖
st.subheader("Machine Data Plot")
fig = plot_data(df)
st.pyplot(fig)