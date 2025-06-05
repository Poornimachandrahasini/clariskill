import streamlit as st

# Set default page if not defined
if 'page' not in st.session_state:
    st.session_state.page = "login"

# Logout handler
if 'logout' in st.session_state and st.session_state.logout:
    st.session_state.page = "login"
    st.session_state.login_success = False
    st.session_state.logout = False
    st.experimental_rerun()

# Navigation logic
if st.session_state.page == "signup":
    import signup
elif st.session_state.page == "main":
    import main_page
else:
    import login
