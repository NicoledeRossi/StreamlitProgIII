import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from utils.carrega_dados import carrega_dados

df = carrega_dados()

st.title('🧬 Perfil de Idade dos Pacientes')
st.markdown("""
A seção de análise por idade! Aqui, exploramos a 
            *distribuição etária dos nossos pacientes* e a 
            *relação da idade com o gênero*.
            
Entenda melhor a composição de idade da nossa base de dados.
""")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/idades.jpg", width=300)

st.markdown("---")
st.subheader("🏥 Mapa das Idades dos Pacientes")
st.markdown("Veja como a **quantidade de pacientes se distribui por cada faixa etária** em nosso conjunto de dados.")

# Contagem de pacientes por idade
contagem_idade = df['Idade'].value_counts().sort_index()
contagem_df = pd.DataFrame({
    'Idade': contagem_idade.index,
    'Quantidade': contagem_idade.values
})

# Gráfico interativo com Plotly
fig_bar = px.bar(contagem_df, x='Idade', y='Quantidade',
                 labels={'Quantidade': 'Número de Pacientes'},
                 title='Número de Pacientes por Idade',
                 color_discrete_sequence=['skyblue'])

st.plotly_chart(fig_bar, use_container_width=True)


# Título da seção do boxplot
st.subheader("📊 Boxplot: Idade por Gênero")
st.markdown(f"""
Este gráfico de boxplot permite visualizar a **distribuição da idade** para cada gênero (Masculino -**M** e Feminino -**F**).
            
Você pode observar a mediana, quartis, valores atípicos e as médias de idade para cada grupo, 
ajudando a identificar padrões ou diferenças significativas.
            

""")

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

# Mensagem de encerramento da página
st.markdown("""
---
Com estes gráficos, esperamos fornecer uma compreensão clara sobre o perfil etário dos nossos pacientes e como ele se relaciona com o gênero.
""")