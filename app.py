import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
from git import Repo
import arrow
import os
import av
import cv2

class Processor(VideoProcessorBase):
    def __init__(self):
        self.points =[]
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = (35, 50, 50)
        upper = (85, 255, 255 )
        mask = cv2.inRange(hsv, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        biggest = max(contours, key=cv2.contourArea)
@st.fragment(run_every="1s")
def show_sidebar_footer():
    repo = Repo(os.getcwd(), search_parent_directories=True)
    repo_url = "https://github.com/nexora-droid/web-cam-parabola/"
    head_commit = repo.head.commit
    commit_hash = head_commit.hexsha
    commit_message = head_commit.message
    commit_author = head_commit.author
    commit_date = head_commit.authored_datetime
    commit_link = f"{repo_url}commit/{commit_hash}"
    st.divider(width="stretch")
    st.markdown("This project is maintained by [@nexora-droid](https://www.github.com/nexora-droid), under a [personal license](https://github.com/nexora-droid/web-cam-parabola/blob/main/LICENSE.md) proihibitng the usage of this project for commerical uses.")
    st.write("All code is publicly available at [the repository](https://github.com/nexora-droid/web-cam-parabola/).")
    st.divider(width="stretch")
    timestamp = commit_date
    past_time = arrow.aget(timestamp)
    relative_time = past_time.humanize()
    st.markdown(f"**Last commit:** [`{commit_hash[:7]}`]({commit_link}), '_{commit_message.strip()}_'   {relative_time} by {commit_author}")

if "nav_page" not in st.session_state:
    st.session_state["nav_page"] = "Home"
with st.sidebar:
    if st.button(label="Home", icon="🏠", use_container_width=True):
        st.session_state["nav_page"] = "Home"
    if st.button(label="FAQ", icon="❓", use_container_width=True):
        st.session_state["nav_page"] = "FAQ"
    if st.button(label="Options", icon="⚙️", use_container_width=True):
        st.session_state["nav_page"] = "Options"
    show_sidebar_footer()
if st.session_state["nav_page"] == "Home":
    st.title("Home")
    st.text("Web-bola is a free, open-source project that runs on Python to track the motion of an object using your webcam and turns it into a parabola graph.")
    st.divider(width="stretch")
    st.subheader("View your camera")
    webrtc_streamer(key="video", media_stream_constraints={"video":True, "audio":False}, video_processor_factory=Processor)
    st.text("Press start to start your camera. If you are using an external camera, remember to select it in the select device option")
if st.session_state["nav_page"] == "FAQ":
    st.title("FAQ")
if st.session_state["nav_page"] == "Options":
    st.title("Options")

