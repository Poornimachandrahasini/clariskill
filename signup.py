import streamlit as st
import json
import os

USER_DB = "users.json"

st.set_page_config(page_title="Sign Up | ClariSkill", layout="centered")
st.title("📝 Create New Account")

username = st.text_input("Choose a Username")
password = st.text_input("Choose a Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Create Account"):
    if not username or not password:
        st.warning("Please fill all fields.")
    elif password != confirm:
        st.error("Passwords do not match.")
    else:
        # Load or create DB
        if os.path.exists(USER_DB):
            with open(USER_DB, "r") as f:
                users = json.load(f)
        else:
            users = {}

        if username in users:
            st.error("Username already exists!")
        else:
            users[username] = password
            with open(USER_DB, "w") as f:
                json.dump(users, f)
            st.success("✅ Account created! Please log in.")
