# 3. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente o valor máximo da coluna do arquivo 'Valor Final'.
import pandas as pd
df1 = pd.read_excel('Vendas.xlsx')
print("Valor máximo: R$%.2f"%df1["Valor Final"].max())