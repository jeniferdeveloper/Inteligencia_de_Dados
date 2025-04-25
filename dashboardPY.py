# pip install streamlit pandas plotly
# streamlit run DashboardPY.py  

import streamlit as st
import pandas as pd
import plotly.express as px

# Confirguração da página
st.set_page_config(layout="wide") # layout wide amplo 
df = pd.read_csv("supermarket_sales.csv", sep=",", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Criação de Filtro Mensal
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month)) # coluna formato YYYY-MM
month = st.sidebar.selectbox("Mês", df["Month"].unique()) # sidebar barra lateral
df_filtered = df[df["Month"] == month] # Filtra o dataframe para conter apenas os dados do mês selecionado

# Layout do Dashboard
col1, col2 = st.columns(2) # Duas colunas na primeira linha: (col1 e col2).
col3, col4, col5 = st.columns(3) # Três colunas na segunda linha: (col3, col4 e col5). 

## Gráfico 1 – Faturamento Diário
fig_date = px.bar(df_filtered,  x="Date", y="Total", color="City", title="Faturamento por dia") # Eixo X: Datas (DATE), Eixo Y: Valor Total (TOTAL), Cores diferenciadas por Cidade (CITY).
col1.plotly_chart(fig_date, use_container_width=True) # Exibe o gráfico na primeira coluna(col1), ajustando-o à largura do contêiner.

#### Gráfico 2 – Faturamento por Tipo de Produto
   ### Cria um gráfico de barras horizontais(orientation=“h”):
   ## Eixo Y: Categorias de produtos(Product line).
   ## Eixo X: Valor Total (TOTAL).
   ## Cores diferenciadas por Cidade (CITY).
fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de Produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True) # Exibe o gráfico na segunda coluna(col2).

#### Gráfico 3 – Faturamento por Filial
    ## Agrupa os dados por cidade(City) e soma os valores(Total).
    ##Cria um gráfico de barras comparando o faturamento entre filiais.
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por Filial")
col3.plotly_chart(fig_city, use_container_width=True) # Exibido na terceira coluna.

#### Gráfico 4 – Forma de Pagamento
    ## Gráfico pizza mostrando a contribuição de cada método de pagamento(Payment) para o faturamento total.
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de Pagamento")
col4.plotly_chart(fig_kind, use_container_width=True) # Exibido na coluna 4(col4).

#### Gráfico 5 – Avaliação por Filial
    ## Calcula a avaliação média(Rating) por filial(City).
    ## Gráfico de barras para comparar a satisfação dos clientes entre cidades.
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)# Exibido na coluna 5(col5).