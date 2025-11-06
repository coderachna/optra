import streamlit as st

def show_mentor():
    st.header("🤖 AI Career Mentor")
    st.write("Type your top skills below to get a career suggestion!")

    skills = st.text_input("Enter your skills:")

    if st.button("Get Suggestion"):
        user_input = skills.lower()

        if "python" in user_input:
            st.success("💼 Recommended Role: Data Analyst or ML Intern")
            st.progress(80)
        elif "web" in user_input:
            st.success("💼 Recommended Role: Frontend Developer")
            st.progress(70)
        elif "java" in user_input:
            st.success("💼 Recommended Role: Backend Developer")
            st.progress(65)
        elif "data" in user_input:
            st.success("💼 Recommended Role: Data Scientist")
            st.progress(90)
        else:
            st.info("🤔 Try adding a skill like Python, Java, or Web!")
