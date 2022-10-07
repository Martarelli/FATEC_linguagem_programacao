# 9. (Função com retorno sem parâmetro) Foi realizada uma pesquisa sobre algumas características físicas de cinco habitantes de uma região. Foram coletados os seguintes dados de cada habitante: idade, sexo (M - masculino ou F - feminino), cor dos olhos (A - azuis ou C - castanhos), cor dos cabelos (L - louros, P - pretos ou C - castanhos).

#    1. Faça uma função/método que leia esses dados, armazenando-os em vetores (listas);
#    2. Faça uma função/método que determine e devolva a função principal a média de idades das pessoas com olhos castanhos e cabelos pretos;
#    3. Faça uma função/método que determine e devolva a função principal a maior idade entre os habitantes;
#    4. Faça uma função/método que determine e devolva a função principal a quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis e cabelos louros.

# Declarar os vetores antes de qualquer programação, indica que 
# que estas variáveis serão globais a todo o restante do programa 
# e das funções 


def cadastrar():
    idade = []
    sexo = []
    olho = []
    cabelo = []
    
    for i in range(5):
        idade.append(int(input("Digite a idade: ")))
        sexo.append(input("sexo (M - masculino ou F - feminino)"))
        olho.append(input("cor dos olhos (A - azuis ou C - castanhos)"))
        cabelo.append(input("cor dos cabelos (L - louros, P - pretos ou C - castanhos)"))
        
    media_cast_preto = 0
    soma_idade = 0
    qtd_cast_preto = 0
    for i in range(5):
        if olho[i].upper() == "C" and cabelo[i].upper() == "P":
            soma_idade += idade[i]
            qtd_cast_preto += 1
    
    media_cast_preto = soma_idade / qtd_cast_preto
    
    maior_idade = 0
    for i in range(5):
        if idade[i] > maior_idade:
            maior_idade = idade[i]
    
    ind_feminino = 0
    for i in range(5):
        if 18 <= idade[i] >= 35 and olho[i].upper() == "A" and cabelo[i].upper() == "L":
            ind_feminino += 1
            
    return media_cast_preto, maior_idade, ind_feminino            
    
def main():
    media, idade_max, fem = cadastrar()
    print("A média de idades das pessoas com olhos castanhos e cabelos pretos:",media)
    print("A maior idade entre os habitantes", idade_max) 
    print("A quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e que tenham olhos azuis e cabelos louros.", fem) 
    
    
main()