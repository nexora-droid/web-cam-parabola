import streamlit as st
from streamlit_webrtc import webrtc_streamer


home = st.Page("main.py", title="Home", icon="🏠")
faq = st.Page("faq.py", title="FAQ", icon="❓")


st.set_page_config(initial_sidebar_state="collapsed")
st.title("Web-bola")
with st.sidebar:
    col1, col2, col3 = st.columns([1,2 ,1])
    with col2:
        st.title("Web-bola")
    st.page_link(home)
    st.page_link(faq)
