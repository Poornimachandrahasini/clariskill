import streamlit as st
import json
import os

# Set page title
st.set_page_config(page_title="Sign Up | ClariSkill", layout="centered")
st.title("📝 Create a New Account")

# Initialize page session state
if "page" not in st.session_state:
    st.session_state.page = "signup"

# Input fields
username = st.text_input("Choose a Username")
password = st.text_input("Choose a Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

# Handle account creation
if st.button("Create Account"):
    if not username or not password:
        st.warning("Please fill all fields.")
    elif password != confirm:
        st.error("Passwords do not match.")
    else:
        # Load existing users or initialize
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                users = json.load(f)
        else:
            users = {}

        # Check if username is taken
        if username in users:
            st.error("Username already exists.")
        else:
            # Save new user
            users[username] = password
            with open("users.json", "w") as f:
                json.dump(users, f)
            st.success("✅ Account created successfully! Please log in.")
            st.session_state.page = "login"
            st.experimental_rerun()

# Go to login
if st.button("Go to Login"):
    st.session_state.page = "login"
    st.experimental_rerun()
