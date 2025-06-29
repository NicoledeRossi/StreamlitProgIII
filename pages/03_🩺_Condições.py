import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.carrega_dados import carrega_dados

# Configurações da página
st.set_page_config(
    page_title='Condições',
    page_icon='📈',
    layout='wide'
)

# Carrega os dados
df = carrega_dados()

# Título principal
st.title("Condições de saúde informada")

# Imagem centralizada
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/consulta4.jpg", width=300)

# Define as condições analisadas
condicoes = ['Hipertensão', 'Diabetes', 'Alcoolismo', 'Deficiência']

# Soma os valores (1 = paciente tem a condição)
somas = df[condicoes].sum()

# Cria DataFrame auxiliar para o gráfico
cond_df = somas.reset_index()
cond_df.columns = ['Condição', 'Quantidade']

# Ordena para melhor visualização
cond_df = cond_df.sort_values(by='Quantidade', ascending=False)

# Cria a figura e o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=cond_df, x='Condição', y='Quantidade', palette='pastel', ax=ax)

# Adiciona os valores no topo das barras
for p in ax.patches:
    altura = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2, altura + 5, int(altura),
            ha='center', va='bottom', fontsize=12)

# Personalização do gráfico
ax.set_title('Quantidade de Pacientes por Condição de Saúde', fontsize=16)
ax.set_ylabel('Número de Pacientes')
ax.set_xlabel('Condição')
plt.tight_layout()

# Exibe o gráfico no Streamlit
st.pyplot(fig)



