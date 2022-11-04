arquivo_escrita = open('./2ºBimestre/Aula 2/exercicio1.txt', 'w')
# arquivo_escrita = open('./2ºBimestre/Aula 2/exercicio1.txt', 'a') adiciona ao final
for linha in range(1,5):
    arquivo_escrita.write("Linha número %i\n" %linha)
    # arquivo_escrita.write("Linha número com append %i\n" %linha)
arquivo_escrita.close()
print("Termino da criação do arquivo....")

arquivo_leitura = open(f'./2ºBimestre/Aula 2/exercicio1.txt', 'r')
for x in arquivo_leitura.readlines():
    print(x)
arquivo_leitura.close()
print("Termino da leitura do arquivo....")

