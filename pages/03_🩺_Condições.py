import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from utils.carrega_dados import carrega_dados


st.set_page_config(
    page_title='Condições',
    page_icon='📈',
    layout='wide'
)

df = carrega_dados()

st.title("Condições de saúde informada")


st.markdown("""        
Aqui exploramos a *prevalência das condições de saúde* mais comuns entre nossos pacientes.
Descubra como essas doenças pré-existentes se distribuem em nossa base de dados.
""")

col1, col2, col3 = st.columns([1, 2, 1])  # Coluna do meio é maior
with col2:
    st.image("assets/consulta4.jpg", width=300)

st.markdown("---")

st.subheader("🏥 Contagem de Pacientes por Condição de Saúde")
st.markdown("""                              
Este gráfico mostra a **quantidade de pacientes** que informaram ter cada uma das seguintes condições:
            
**Hipertensão**, **Diabetes**, **Alcoolismo** e **Deficiência**.
            
""")

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



st.markdown("---")
st.subheader("📌 Distribuição de Doenças por Idade e Gênero")
st.markdown("""
Explore a relação entre **condições médicas**, **idade dos pacientes** e **gênero**.
Você pode selecionar a condição de saúde desejada para analisar sua distribuição.
""")
# Criação da coluna de Faixa Etária
bins = [0, 9, 19, 29, 39, 49, 59, 69, float('inf')]
labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']
df['Faixa Etária'] = pd.cut(df['Idade'], bins=bins, labels=labels, right=True)

doenca_escolhida = st.selectbox("Selecione uma condição médica:", ['Hipertensão', 'Diabetes', 'Alcoolismo', 'Deficiência'])

# Filtra os pacientes com a doença escolhida
df_doenca = df[df[doenca_escolhida] == 1]

# Conta por faixa etária e gênero
contagem = df_doenca.groupby(['Faixa Etária', 'Gênero']).size().reset_index(name='Quantidade')

# Gráfico de barras empilhadas
fig = px.bar(
    contagem,
    x='Faixa Etária',
    y='Quantidade',
    color='Gênero',
    title=f'Distribuição de {doenca_escolhida} por Faixa Etária e Gênero',
    labels={'Quantidade': 'Número de Pacientes'},
    color_discrete_map={'F': 'deeppink', 'M': 'blue'}
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
---
Com base nesta análise, podemos entender melhor o perfil de saúde dos pacientes atendidos.
""")
