import streamlit as st
import pandas as pd
import plotly.express as px
from utils.carrega_dados import carrega_dados

st.set_page_config(
    page_title='Condições',
    page_icon='📈',
    layout='wide'
)

df = carrega_dados()

st.title("✅ Análise de Comparecimento às Consultas")
st.markdown(f"""
Bem-vindo a esta seção crucial! Aqui, investigamos o **comportamento de comparecimento dos pacientes às consultas**.
Vamos analisar a taxa geral de comparecimento e, em seguida, como o recebimento de SMS impacta essa presença.
""")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/consulta2.jpg", width=300)

st.markdown("---")

# Mostra distribuição para conferência
st.subheader("Distribuição de Comparecimento")
st.write(df['Faltou a Consulta'].value_counts())

# Seção 1: Distribuição de Comparecimento Geral
st.subheader("📊 Taxa Geral de Comparecimento")
st.markdown(f"""
Entenda a **proporção de pacientes que compareceram ou faltaram** às consultas agendadas.
""")

# Garante o tipo correto
df['Faltou a Consulta'] = df['Faltou a Consulta'].astype(str)
df['Compareceu à Consulta'] = df['Faltou a Consulta'].map({'Sim': 'Não', 'Não': 'Sim'})

# Gráfico interativo com Plotly
fig1 = px.histogram(df, x='Compareceu à Consulta', color='Compareceu à Consulta',
                    color_discrete_sequence=px.colors.qualitative.Set2,
                    title='Quantidade de Pacientes que Compareceram à Consulta',
                    text_auto=True)

fig1.update_layout(
    xaxis_title='Compareceu à Consulta',
    yaxis_title='Número de Pacientes',
    showlegend=False
)

st.plotly_chart(fig1, use_container_width=True)

# Seção 2: Impacto do SMS
st.markdown("---")
st.subheader("📩 Impacto do Recebimento de SMS no Comparecimento")
st.markdown(f"""
Este gráfico mostra a *relação entre o recebimento de SMS e o comparecimento às consultas*.
Veja se o envio de SMS faz diferença na presença dos pacientes.
""")

# Ajustes de colunas
df['SMS Recebido'] = df['SMS Recebido'].map({0: 'Não Recebeu SMS', 1: 'Recebeu SMS'})
df['Faltou a Consulta'] = df['Faltou a Consulta'].astype(str)

# Gráfico interativo de barras empilhadas
fig2 = px.histogram(df, x='SMS Recebido', color='Faltou a Consulta',
                    barmode='stack',
                    color_discrete_map={'Sim': 'salmon', 'Não': 'skyblue'},
                    title='Recebimento de SMS e Comparecimento à Consulta',
                    text_auto=True)

fig2.update_layout(
    xaxis_title='Grupo de Pacientes',
    yaxis_title='Número de Pacientes',
    legend_title='Faltou à Consulta'
)

st.plotly_chart(fig2, use_container_width=True)

# Rodapé da seção
st.markdown("""
---
Esses insights são fundamentais para otimizar nossas estratégias de comunicação e gestão de agendamentos,
visando melhorar a taxa de comparecimento dos pacientes.
""")
