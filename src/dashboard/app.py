import streamlit as st
import pandas as pd
import sqlite3

#conectar o banco de dados
conn = sqlite3.connect('../data/quotes.db')

#carregar o dados em Dataframe no pandas
df = pd.read_sql_query('SELECT * FROM mercadolivre_items', conn)
conn.close()

# Título da aplicação
st.title('Pesquisa de mercado no MERCADO LIVRE')

#Criando Layout
st.subheader('KPIs Principais da pagina do sistema')
col1,col2,col3 = st.columns(3)

#Calculando quanto colunas vão aparecer
total_columns = df.shape[0]
col1.metric(label='Número Total de Itens', value= total_columns)

#Calculando quantas marcas aparecem 
total_brands = df['brand'].nunique()
col2.metric(label='Número Total de Marcas', value= total_brands)

#Calculando quanto colunas vão aparecer
media_preco = df['new_price'].mean()
col3.metric(label='Preço Médio R$:  ', value =f'{media_preco:.2f}' )

st.write(df)

#Marcas mais encontradas até a pagina 10
st.subheader('Marcas mais encontradas')
col1, col2 = st.columns([4,2])

# TOP 10 marcas
top_10 = df['brand'].value_counts().sort_values(ascending=False)

col1.bar_chart(top_10)
col2.write(top_10)

# Preço medio por marca
st.subheader('Preço Médio por Marca')
col1,col2 = st.columns([4,2])
df_non_zero_prices = df[df['new_price'] > 0]
mediaPreco_marca = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(mediaPreco_marca)
col2.write(mediaPreco_marca)

# Marca melhor avaliada
st.subheader('Satisfação por Marca')
col1,col2 = st.columns([4,2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfacao_by_marca = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfacao_by_marca)
col2.write(satisfacao_by_marca)
