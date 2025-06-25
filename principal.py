import streamlit as st
from utils.carrega_dados import carrega_dados

st.set_page_config(
    page_title="Frequencia Pacientes em Consultas",
    page_icon="✨",
    layout="wide"
)

st.title("Frequencia Pacientes em Consultas")

df = carrega_dados()

