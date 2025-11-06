import streamlit as st
import dashboard
import mentor
import projects

st.set_page_config(page_title="OPTRA", page_icon="🎯", layout="wide")

st.title("🎯 OPTRA - Smart Career & Opportunity Platform")
st.write("Your one-stop platform for career guidance and opportunities!")

tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🤖 AI Career Mentor", "🧩 Projects"])

with tab1:
    dashboard.show_dashboard()
with tab2:
    mentor.show_mentor()
with tab3:
    projects.show_projects()

st.caption("Made with ❤️ by Team WIFEM")
