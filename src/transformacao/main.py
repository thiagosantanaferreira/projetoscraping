import pandas as pd
import sqlite3
from datetime import datetime

#Transormando o arquivo data.jsonl em Dataframe com o pandas
df = pd.read_json('data\data.jsonl', lines= True)

# Adicionar novas colunas no Dataframe
df['_source'] =  "https://lista.mercadolivre.com.br/tenis-de-corrida-masculino"
df['_data_coleta'] = datetime.now()

#Tratando valores nulos para numerico e texto -> onde o valor for Nulo cola zero 0.00
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(1).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(1).astype(float)

#Remover os parenteser do review amount
df['reviewa_amount'] = df['reviewa_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(int)

#Tratar os preços
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100
#Removendo as colunas não necessarias
df = df.drop(columns=['old_price_reais','old_price_centavos','new_price_reais','new_price_centavos'])

conn = sqlite3.connect('data/quotes.db')
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)
conn.close()

print(df.head())