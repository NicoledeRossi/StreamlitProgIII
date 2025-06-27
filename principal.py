import streamlit as st
#from utils.carrega_dados import carregar_dados

st.set_page_config(
    page_title="Frequencia Pacientes em Consultas",
    page_icon="🏠",
    layout="wide"
)

<<<<<<< Updated upstream
st.title("Frequencia Pacientes em Consultas")
=======
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

* **📊 Dashboard de Análise:** Explore a distribuição de tecnologias, cargos e outras métricas gerais.
* **📈 Salários & Tendências:** Mergulhe em análises salariais, entendendo as remunerações por diferentes fatores.
* **📝 Relatórios Detalhados:** Acesse insights mais aprofundados sobre tópicos específicos.
            


Agradecemos a sua visita e esperamos que encontre informações valiosas aqui!
""")

st.header("Resumo dos Principais Dados")
st.dataframe(df.head())



>>>>>>> Stashed changes
