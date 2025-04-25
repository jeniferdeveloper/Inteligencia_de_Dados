import streamlit as st
import pandas as pd
import plotly.express as px

# 1 Pandas: carrega a manipula os dados
df = pd.DataFrame({
    'País': ['Brasil', 'EUA', 'Alemanha'],
    'PIB (US$)': [1.6e12, 21.4e12, 3.8e12] # e12 elevado a 12
})

# 2 Plotly: cria um grafico
fig = px.bar(df, x='País', y='PIB (US$)', title='PIB por País')

# 3 Streamlit: Exibe tudo no app
st.title("Análise Econômica")
st.write("Dados carregados:")
st.dataframe(df)
st.plotly_chart(fig)