import streamlit as st
import matplotlib.pyplot as plt
from utils.carrega_dados import carrega_dados


st.set_page_config(
    page_title='Condições',
    page_icon='"🧬',
    layout='wide'
)

df = carrega_dados()

st.title('📊 Idade dos Pacientes')

col1, col2, col3 = st.columns([1, 2, 1])  # Coluna do meio é maior
with col2:
    st.image("assets/idades.jpg", width=300)

# Contagem de pacientes por idade
contagem_idade = df['Idade'].value_counts().sort_index()

# Criar a figura
fig, ax = plt.subplots(figsize=(12, 6))
contagem_idade.plot(kind='bar', color='skyblue', ax=ax)

# Títulos e rótulos
ax.set_xlabel('Idade')
ax.set_ylabel('Número de Pacientes')
ax.set_title('Número de Pacientes por Idade')
ax.grid(axis='y')

# Ajustar o layout
plt.tight_layout()

# Exibir no Streamlit
st.pyplot(fig)

st.title("Boxplot Idade x Genero")

# Filtrando os dados
idades_m = df[df['Gênero'] == 'M']['Idade']
idades_f = df[df['Gênero'] == 'F']['Idade']

# Cálculo das médias
media_m = idades_m.mean()
media_f = idades_f.mean()

# Criando a figura do boxplot
fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot([idades_m, idades_f], patch_artist=True,
           boxprops=dict(facecolor='lightblue'),
           labels=['M', 'F'])

# Linhas da média
ax.axhline(media_m, color='blue', linestyle='--', label=f'Média Masculino = {media_m:.2f}')
ax.axhline(media_f, color='magenta', linestyle='--', label=f'Média Feminino = {media_f:.2f}')

# Customizações
ax.set_title("Boxplot da Idade por Gênero", fontsize=14)
ax.set_ylabel("Idade", fontsize=12)
ax.grid(axis='y', linestyle=':', alpha=0.7)
ax.legend()

# Mostrar o gráfico no Streamlit
st.pyplot(fig)