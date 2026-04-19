import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.markdown("""
    <style>
    div.stButton > button > div > p {
        text-align: left;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
if "page" not in st.session_state:
    st.session_state = "Home"
with st.sidebar:
    if st.button(label="Home", icon="🏠", use_container_width=True):
        st.session_state = "Home"
    if st.button(label="FAQ", icon="❓", use_container_width=True):
        st.session_state = "FAQ"
    if st.button(label="Options", icon="⚙️", use_container_width=True):
        st.session_state = "Options"
    st.divider(width="stretch")
    st.markdown("This project is maintained by [@nexora-droid](https://www.github.com/nexora-droid), under a [personal license](https://github.com/nexora-droid/web-cam-parabola/blob/main/LICENSE.md) proihibitng the usage of this project for commerical uses.")
    st.write("All code is publicly available at [the repository](https://github.com/nexora-droid/web-cam-parabola/).")
if st.session_state == "Home":
    st.title("Home")
    st.text("Web-bola is a free, open-source project that runs on Python to track the motion of an object using your webcam and turns it into a parabola graph.")
if st.session_state == "FAQ":
    st.title("FAQ")
if st.session_state == "Options":
    st.title("Options")