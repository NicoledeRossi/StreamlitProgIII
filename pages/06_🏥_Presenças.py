import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.carrega_dados import carrega_dados

# Configuração da página
st.set_page_config(
    page_title='Condições',
    page_icon='📈',
    layout='wide'
)

# Carregamento dos dados
df = carrega_dados()

# Título e imagem
st.title("Compareceram às Consultas")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/consulta2.jpg", width=300)

# -----------------------------
# PARTE 1: Gráfico de Comparecimento
# -----------------------------

# Garantir tipo de dado adequado
df['Faltou a Consulta'] = df['Faltou a Consulta'].astype(str)

# Criar nova coluna invertida
df['Compareceu à Consulta'] = df['Faltou a Consulta'].map({'Sim': 'Não', 'Não': 'Sim'})

# Mostrar contagem no app
st.subheader("Distribuição de Comparecimento")
st.write(df['Compareceu à Consulta'].value_counts())

# Gráfico de barras simples
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.countplot(data=df, x='Compareceu à Consulta', palette='Set2', ax=ax1)

# Adiciona números nas barras
for p in ax1.patches:
    altura = p.get_height()
    ax1.text(p.get_x() + p.get_width() / 2, altura + 0.5, int(altura),
             ha='center', va='bottom', fontsize=12)

# Personalização do gráfico
ax1.set_title('Quantidade de Pessoas que Compareceram à Consulta')
ax1.set_xlabel('Compareceu à Consulta')
ax1.set_ylabel('Número de Pacientes')
plt.tight_layout()

st.pyplot(fig1)

# -----------------------------
# PARTE 2: Gráfico SMS vs Faltas
# -----------------------------

# Transformar valores para leitura mais clara
df['SMS Recebido'] = df['SMS Recebido'].map({0: 'Não Recebeu SMS', 1: 'Recebeu SMS'})

# Tabela cruzada: SMS × Faltou
tabela = df.groupby(['SMS Recebido', 'Faltou a Consulta']).size().unstack()
tabela = tabela.reindex(['Não Recebeu SMS', 'Recebeu SMS'])  # ordenação lógica

# Gráfico empilhado
fig2, ax2 = plt.subplots(figsize=(8, 6))
tabela.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax2)

# Customização do gráfico
ax2.set_title('Recebimento de SMS e Comparecimento à Consulta')
ax2.set_xlabel('Grupo de Pacientes')
ax2.set_ylabel('Número de Pacientes')
ax2.legend(title='Faltou à Consulta')
ax2.set_xticklabels(tabela.index, rotation=0)

# Adiciona rótulos de valor dentro das barras + total no topo
for i, row in enumerate(tabela.values):
    y_offset = 0
    for value in row:
        ax2.text(i, y_offset + value / 2, int(value),
                 ha='center', va='center', fontsize=9)
        y_offset += value
    total = sum(row)
    ax2.text(i, y_offset + 5, f'Total: {int(total)}',
             ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

plt.tight_layout()
st.pyplot(fig2)
