import pandas as pd
import streamlit as st
import requests

@st.cache_data
def carrega_dados():
    df = pd.read_csv('./dataset/KaggleV2-May-2016.csv', skiprows=[1])
    df = df.drop(columns='PatientId')
    df = df.drop(columns='AppointmentID')
    df = df.drop(columns='Scholarship')
    df = df.rename(columns={
    'Gender': 'Gênero',
    'ScheduledDay': 'Dia Agendado',
    'AppointmentDay': 'Dia da Consulta',
    'Age': 'Idade',
    'Neighbourhood': 'Bairro',
    'Hipertension': 'Hipertensão',
    'Diabetes': 'Diabetes',
    'Alcoholism': 'Alcoolismo',
    'Handcap': 'Deficiência',
    'SMS_received': 'SMS Recebido',
    'No-show': 'Faltou a Consulta'
    })
    df['Dia Agendado'] = pd.to_datetime(df['Dia Agendado'])
    df['Dia da Consulta'] = pd.to_datetime(df['Dia da Consulta'])
    df['Dia da Consulta'].dt.time.unique()
    df['Dia da Consulta'] = df['Dia da Consulta'].dt.strftime('%d/%m/%Y')
    df.insert( df.columns.get_loc('Dia Agendado') + 1,'Horario Agendado', df['Dia Agendado'].dt.time)
    df['Dia Agendado'] = df['Dia Agendado'].dt.strftime('%d/%m/%Y')
    df['Faltou a Consulta'] = df['Faltou a Consulta'].replace({'Yes': 'Sim','No': 'Não'})  

    return df  
