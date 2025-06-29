import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.carrega_dados import carrega_dados


st.set_page_config(
    page_title='Condições',
    page_icon='📈',
    layout='wide'
)


df = carrega_dados()


st.title("Condições de saúde informada")

col1, col2, col3 = st.columns([1, 2, 1])  # Coluna do meio é maior

with col2:
    st.image("assets/consulta4.jpg", width=300)

# Seleciona as colunas das condições
condicoes = ['Hipertensão', 'Diabetes', 'Alcoolismo', 'Deficiência']

# Soma quantos pacientes têm cada condição (considerando 1 = tem)
somas = df[condicoes].sum()

# Cria um DataFrame auxiliar para plotar
cond_df = somas.reset_index()
cond_df.columns = ['Condição', 'Quantidade']

# Plotando com seaborn
plt.figure(figsize=(10, 6))
ax = sns.barplot(data=cond_df, x='Condição', y='Quantidade', palette='pastel')
# Criar a figura e o gráfico
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=cond_df, x='Condição', y='Quantidade', palette='pastel', ax=ax)


# Adiciona os números em cima das barras
for p in ax.patches:
    altura = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2, altura + 5, int(altura),
            ha='center', va='bottom', fontsize=12)

ax.set_title('Quantidade de Pacientes por Condição de Saúde')

ax.set_ylabel('Número de Pacientes')
ax.set_xlabel('Condição')
plt.tight_layout()


st.pyplot(fig)

