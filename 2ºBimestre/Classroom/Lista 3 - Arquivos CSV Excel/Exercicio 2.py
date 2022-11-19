# 2. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente a quantidade mínima da coluna do arquivo 'Quantidade'.
import pandas as pd
df1 = pd.read_excel('Vendas.xlsx')
print("Quantidade minima: %i"%df1["Quantidade"].min())