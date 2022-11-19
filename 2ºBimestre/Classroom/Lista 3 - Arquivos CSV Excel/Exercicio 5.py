# 5. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Gere um histograma, referente a coluna Vendas, utilizando a biblioteca plotly.
import pandas as pd
import plotly.express as px

df1 = pd.read_csv('Propaganda.csv')

fig = px.histogram(df1, x="Vendas")
fig.show()