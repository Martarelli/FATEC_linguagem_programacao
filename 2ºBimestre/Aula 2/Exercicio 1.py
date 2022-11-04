arquivo = open('./2ºBimestre/Aula 2/exercicio1.txt', 'w')
for linha in range(1,21):
    arquivo.write("Linha número %i\n" %linha)
arquivo.close()