import streamlit as st

def show_projects():
    st.header("🧩 Student Projects & Collaboration")
    st.write("Here are some example projects students can join:")

    projects = [
        {"Project": "Placement Predictor", "Mentor": "Dr. Singh"},
        {"Project": "AI Resume Analyzer", "Mentor": "Prof. Rao"},
        {"Project": "Interview Prep App", "Mentor": "Ms. Sharma"},
    ]

    st.table(projects)
    st.write("⭐ More exciting projects coming soon!")
