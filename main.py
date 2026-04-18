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