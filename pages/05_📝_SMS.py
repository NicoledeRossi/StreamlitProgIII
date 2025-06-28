import streamlit as st
import matplotlib.pyplot as plt
from utils.carrega_dados import carrega_dados

st.set_page_config(
    page_title='Condições',
    page_icon='📈',
    layout='wide'
)

df = carrega_dados()

st.title("Mensagem de Confirmação de Consulta")

col1, col2, col3 = st.columns([1, 2, 1])  # Coluna do meio é maior
with col2:
    st.image("assets/mensagem.jpg", width=300)


# Contagem de SMS recebidos
contagem_sms = df['SMS Recebido'].value_counts()

# Mapeia os rótulos para deixar mais claro
rotulos = ['Não Recebeu', 'Recebeu']  # Certifique-se que o index 0 = Não, 1 = Sim

# Criando a figura
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(contagem_sms, labels=rotulos, autopct='%1.1f%%',
       colors=['lightcoral', 'lightgreen'], startangle=140)

ax.set_title('Distribuição de SMS Recebidos')
ax.axis('equal')  # Deixa o gráfico redondo
plt.tight_layout()

# Exibir no Streamlit
st.pyplot(fig)