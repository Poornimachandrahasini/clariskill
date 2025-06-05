import streamlit as st
import json

st.title("🔐 Login to ClariSkill")
st.write("Don't have an account? [Sign Up](#)", unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except:
        users = {}

    if username in users and users[username] == password:
        st.success("Login successful! 🎉")
        st.session_state.login_success = True
        st.session_state.username = username
        st.session_state.page = "main"
        st.experimental_rerun()
    else:
        st.error("Invalid username or password")

if st.button("Go to Sign Up"):
    st.session_state.page = "signup"
    st.experimental_rerun()
