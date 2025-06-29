import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.carrega_dados import carrega_dados

st.set_page_config(Add commentMore actions
    page_title='Condições',
    page_icon='📈',
    layout='wide'
)


df = carrega_dados()

st.title("Compareceram as Consultas")

col1, col2, col3 = st.columns([1, 2, 1])  # Coluna do meio é maior
with col2:
    st.image("assets/consulta2.jpg", width=300)





# Garante que a coluna está como string (evita erros de tipo)
df['Faltou a Consulta'] = df['Faltou a Consulta'].astype(str)

# Mapeia: invertendo o significado
df['Compareceu à Consulta'] = df['Faltou a Consulta'].map({'Sim': 'Não', 'Não': 'Sim'})

# Mostra distribuição para conferência
st.subheader("Distribuição de Comparecimento")
st.write(df['Compareceu à Consulta'].value_counts())

# Gera o gráfico
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=df, x='Compareceu à Consulta', palette='Set2', ax=ax)

# Adiciona os valores em cima das barras
for p in ax.patches:
    altura = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2, altura + 0.5, int(altura),
            ha='center', va='bottom', fontsize=12)

# Personalizações
ax.set_title('Quantidade de Pessoas que Compareceram à Consulta')
ax.set_xlabel('Compareceu à Consulta')
ax.set_ylabel('Número de Pacientes')
plt.tight_layout()

# Exibe no Streamlit
st.pyplot(fig)




# Garante que os dados estão no formato correto
df['SMS Recebido'] = df['SMS Recebido'].map({0: 'Não Recebeu SMS', 1: 'Recebeu SMS'})
df['Faltou a Consulta'] = df['Faltou a Consulta'].astype(str)

# Agrupamento por SMS x Faltou
tabela = df.groupby(['SMS Recebido', 'Faltou a Consulta']).size().unstack()


# Ordenar o índice para manter a ordem lógica
tabela = tabela.reindex(['Não Recebeu SMS', 'Recebeu SMS'])


# Criação da figura
fig, ax = plt.subplots(figsize=(8, 6))
tabela.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax)




# Títulos e rótulos
ax.set_title('Recebimento de SMS e Comparecimento à Consulta')
ax.set_xlabel('Grupo de Pacientes')
ax.set_ylabel('Número de Pacientes')
ax.legend(title='Faltou à Consulta')
ax.set_xticklabels(tabela.index, rotation=0)

# Adiciona os números dentro das barras e o total acima
for i, row in enumerate(tabela.values):
    y_offset = 0
    for value in row:
        ax.text(i, y_offset + value / 2, int(value),
                ha='center', va='center', fontsize=9)
        y_offset += value
    total = sum(row)
    ax.text(i, y_offset + 5, f'Total: {int(total)}',
            ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

plt.tight_layout()

# Exibir no Streamlit
st.pyplot(fig)