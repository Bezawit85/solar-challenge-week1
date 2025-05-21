import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import load_data, plot_boxplot

st.title("Solar Metrics Dashboard 🌞")

selected_countries = st.multiselect(
    "Select countries to compare:",
    ["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

metric = st.selectbox("Select metric", ["GHI", "DNI", "DHI"])

if selected_countries:
    df = load_data(selected_countries)
    st.pyplot(plot_boxplot(df, metric, selected_countries))
