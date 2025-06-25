import pandas as pd
import streamlit as st
import requests

@st.cache_data
def carrega_dados():
    df = pd.read_csv('./dataset/KaggleV2-May-2016.csv')