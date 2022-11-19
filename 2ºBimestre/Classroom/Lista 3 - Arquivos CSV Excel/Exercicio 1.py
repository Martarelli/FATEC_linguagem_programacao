# 1. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente a média da coluna do arquivo 'Valor Unitário'.
import pandas as pd
df1 = pd.read_excel('Vendas.xlsx')
print("Media valores unitarios: R$%.2f"%df1["Valor Unitário"].mean())