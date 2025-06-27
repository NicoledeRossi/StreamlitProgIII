import streamlit as st
import plotly.express as px
import pandas as pd
from utils.carrega_dados import carrega_dados

df = carrega_dados()