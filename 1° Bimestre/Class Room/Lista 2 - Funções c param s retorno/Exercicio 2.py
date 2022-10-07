# 2. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método, sem parâmetro, que leia um nome e diga 'Olá nome, tudo bem?'. Crie outra função com o parâmetro nome, para que a mesma receba da main o nome digitado e apresente a mesma frase, este é um exemplo de PASSAGEM DE PARÂMETRO POR VALOR.
def nome(s):
    print("Olá %s, tudo bem? - COM PARAMETRO"%s);

def print_nome():
    name = input("Digite seu nome: ");
    print("Olá %s, tudo bem? - SEM PARAMETRO"%name);

def main():
    print_nome();
    name = input("Digite seu nome: ");
    nome(name);

main();