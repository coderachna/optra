import streamlit as st
import pandas as pd

def show_dashboard():
    st.header("📈 Placement Dashboard")

    # Load data
    df = pd.read_csv("Optra_Prototype/data/placements.csv")

    st.subheader("Placement Data")
    st.dataframe(df)

    # KPIs
    total = df["Students_Placed"].sum()
    avg = df["Average_Package"].mean()
    st.metric("Total Students Placed", total)
    st.metric("Average Package (LPA)", f"{avg:.1f}")

    # Bar chart
    st.subheader("Company-wise Placement Count")
    st.bar_chart(df.set_index("Company")["Students_Placed"])

    # Leaderboard (mock)
    st.subheader("🏅 Leaderboard")
    st.table({
        "Name": ["Riya", "Aarav", "Neha", "Arjun"],
        "XP": [1200, 950, 800, 700]
    })
