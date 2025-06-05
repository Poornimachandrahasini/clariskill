import streamlit as st
import json

st.set_page_config(page_title="Login | ClariSkill", layout="centered")

if 'login_success' not in st.session_state:
    st.session_state.login_success = False

st.title("🔐 Welcome to ClariSkill")
st.write("Please log in to continue or [Sign Up](signup.py)")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except:
        users = {}

    if username in users and users[username] == password:
        st.session_state.login_success = True
        st.session_state.username = username
        st.success("Login successful! 🎉")
        st.experimental_rerun()
    else:
        st.error("Invalid username or password")

if st.session_state.login_success:
    import main_page  # this will run your skill dashboard
