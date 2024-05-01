import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

# df = pd.read_pickle("file.pkl")

## importing the model
# pipe = pickle.load(open('pipe.pkl','rb'))
# df = pickle.load(open('df.pkl','rb'))
pipe = pd.read_pickle("pipe.pkl")
df = pd.read_pickle("df.pkl")

st.title('Laptop Price Predictor')

##----------------- Creating a form for the user--------------------------

## Brand name
company = st.selectbox('Brand', df['Company'].unique())

## Type of Laptop
laptopType = st.selectbox('Type', df['TypeName'].unique())

## RAM size
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16])

## Weight of laptop
weight = st.number_input('Weight of the Laptop(in kg)')

## Touchscreen Laptop or not
touchscreen = st.selectbox('Touchscreen',['Yes','No'])

## IPS display or not
IPS = st.selectbox('IPS',['Yes','No'])

## Screen Size
screen_size = st.number_input('Screen Size')

## Resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

## CPU Brand
cpu = st.selectbox('CPU',df['CPU_Brand_Name'].unique())

## HardDrive
HDD = st.selectbox('HDD(in GB)',[0,128,256,512,1024])

## SSD
ssd = st.selectbox('SSD(in GB)',[0,128,256,512,1024])

## GPU
gpu = st.selectbox('GPU Brand',df['GPU'].unique())

## Operating System
os = st.selectbox('Operating System',df['OperatingSystem'].unique())

if st.button('Predict Price'):
    ppi = None

    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if IPS == 'Yes':
        IPS = 1
    else:
        IPS = 0

    ## Calculating PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[0])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5/screen_size

    query = np.array([company, laptopType, ram, weight, touchscreen, IPS, ppi, cpu, HDD, ssd, gpu, os], dtype=object)

    query = query.reshape(1, 12)
    st.title("The Predicted price of your desired laptop is Rs." + str(int(np.exp(pipe.predict(query)[0]))))