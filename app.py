import subprocess
import sys
import streamlit as st
import run_with_webcam
import time

st.title("Gaze Predictor")

def start_capture():
    subprocess.run([f"{sys.executable}", "run_with_webcam.py"])

if st.button("Start Capturing Gaze"):
    st.write(start_capture())

