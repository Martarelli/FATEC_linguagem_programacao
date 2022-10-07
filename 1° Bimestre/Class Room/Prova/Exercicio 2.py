# 2. [1,50 ponto] Faça uma função que receba como parâmetro uma frase, conte e apresente:

# a) quantas vogais;

# b) quantas consoantes;

# c) e quantos números tem na frase.

# Lembrete, quando um parâmetro é um vetor, este na programação, é chamado de PASSAGEM DE PARÂMETRO POR REFERÊNCIA.

def contagem(str):
    tot_vogais = 0
    tot_cons= 0
    tot_num = 0
    for i in str:
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
            tot_vogais += 1
        if (i != "a" and i != "e" and i != "i" and i != "o" and i !="u") and not i.isdecimal():
            tot_cons += 1
        if i.isnumeric():
            tot_num += 1
            
    print("Total de vogais: ", tot_vogais)
    print("Total de consoantes: ", tot_cons)
    print("Total de números: ", tot_num)
    
def main():
    frase = input("Digita uma frase...: ").lower()
    contagem(frase)
    
main ()