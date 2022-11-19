# 6. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Gere um histograma, referente a coluna TV, utilizando a biblioteca Matplotlib, apresente na cor verde.

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df1 = pd.read_csv('Propaganda.csv')

plt.hist(df1["TV"], 12 , rwidth=0.75, color="green")
plt.title("Propaganda Via TV")
plt.xlabel("Custo")
plt.ylabel("Frequência Absoluta")
plt.show()