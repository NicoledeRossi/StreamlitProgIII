import streamlit as st
from utils.carrega_dados import carrega_dados

st.set_page_config(
    page_title="Frequencia Pacientes em Consultas",
    page_icon="🏠",
    layout="wide"
)

st.title("Frequencia Pacientes em Consultas")

df = carrega_dados()


st.image("assets/consulta.jpg", width=300)


st.markdown(f"""
Bem-vindo(a) ao **Balcao de Consultas**!

Este aplicativo interativo foi desenvolvido para visualizar os dados de um dashboard mostrando a frequencia de pacientes a cosnultas marcadas.
            
O seu conjunto de dados tem as seguintes dimensões:
- **Linhas:** `{df.shape[0]}` 📊
- **Colunas:** `{df.shape[1]}` 📈


---

### Como Navegar:

Utilize o menu de navegação na **barra lateral (esquerda)** para explorar as diferentes seções do aplicativo:
Cada seção apresenta gráficos, análises e informações específicas relacionadas à frequência dos pacientes em consultas.

- Dashboard principal com gráficos de presença e ausência.

- Análises de condições médicas, faixas etárias e outras variáveis.

- Relatórios detalhados com dados complementares.

 ---           
Agradecemos a sua visita e esperamos que encontre informações valiosas aqui!
""")







