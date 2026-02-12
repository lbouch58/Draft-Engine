import streamlit as st
import pandas as pd

st.set_page_config(page_title="Draft Engine", layout="wide")

st.title("Fantasy Draft Engine 🏈")

# Load cleaned projections
@st.cache_data
def load_data():
    return pd.read_csv("data/clean/fantasypros_2024_2025_projections.csv")

df = load_data()

st.sidebar.header("Filters")

season = st.sidebar.selectbox("Season", sorted(df["season"].unique(), reverse=True))
position = st.sidebar.selectbox("Position", ["All"] + sorted(df["position"].unique()))

filtered = df[df["season"] == season]

if position != "All":
    filtered = filtered[filtered["position"] == position]

st.subheader("Available Players")

st.dataframe(
    filtered.sort_values("proj_points_ppr", ascending=False),
    use_container_width=True
)
