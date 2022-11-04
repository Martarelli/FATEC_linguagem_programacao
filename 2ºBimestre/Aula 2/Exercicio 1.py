arquivo = open('./2ºBimestre/Aula 2/exercicio1.txt', 'a')
for linha in range(1,5):
    arquivo.write("Linha número com append %i\n" %linha)
arquivo.close()