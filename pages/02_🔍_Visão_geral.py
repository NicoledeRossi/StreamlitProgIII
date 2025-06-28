import streamlit as st
import matplotlib.pyplot as plt
from utils.carrega_dados import carrega_dados

st.set_page_config(
    page_title='Visão Geral',
    page_icon='📈',
    layout='wide'
)

df = carrega_dados()

st.title("Resumo dos Principais Dados")
st.dataframe(df.head())

st.subheader('📊 Contar pacientes por gênero')
col1, col2, col3 = st.columns([1, 2, 1])  # Coluna do meio é maior
with col2:
    st.image("assets/hxm.jpg", width=300)

# Contar pacientes únicos por gênero
contagem_pacientes = df.groupby('Gênero')['ID do Paciente'].nunique()

# Renomear os índices para exibir no gráfico
contagem_pacientes.index = contagem_pacientes.index.map({'M': 'Homens', 'F': 'Mulheres'})

# Cores conforme pedido
cores = {'Mulheres': 'pink', 'Homens': 'blue'}

# Criar figura e eixo
fig, ax = plt.subplots(figsize=(6, 4))

# Plotar o gráfico de barras
contagem_pacientes.plot(kind='bar', color=[cores.get(g, 'gray') for g in contagem_pacientes.index], ax=ax)

# Títulos e rótulos
ax.set_title('Número de Pacientes Únicos por Gênero')
ax.set_xlabel('Gênero')
ax.set_ylabel('Número de Pacientes')
ax.set_xticklabels(contagem_pacientes.index, rotation=0)
ax.grid(axis='y')

# Adicionar os números sobre as barras
for p in ax.patches:
    altura = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2, altura + 0.5, int(altura), ha='center')

# Ajuste do layout
plt.tight_layout()

# Exibir o gráfico no Streamlit
st.pyplot(fig)
