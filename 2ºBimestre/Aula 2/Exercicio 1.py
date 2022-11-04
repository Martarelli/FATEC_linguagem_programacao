arquivo = open('./2ºBimestre/Aula 2/exercicio1.txt', 'w')
# arquivo = open('./2ºBimestre/Aula 2/exercicio1.txt', 'a') adiciona ao final
for linha in range(1,5):
    arquivo.write("Linha número com append %i\n" %linha)
    # arquivo.write("Linha número com append %i\n" %linha)
arquivo.close()
print("Termino de execução....")