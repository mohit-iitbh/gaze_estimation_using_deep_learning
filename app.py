import subprocess
import sys
import streamlit as st
import run_with_webcam

def start_capture():
    subprocess.run([f"{sys.executable}", "run_with_webcam.py"])

if st.button("Start Capturing"):
    st.write(start_capture())


st.write(run_with_webcam.main)
