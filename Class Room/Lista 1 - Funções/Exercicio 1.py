# 1. (Função sem retorno sem parâmetro) Faça um programa contendo uma função/método que apresente o valor 1 se o número digitado for positivo e 0 se for negativo.

def apresentar_mensagem():
    print("Olá, tudo bem?");
    numero = int(input("Digite um número para ser analisado: "));

    if numero >= 0:
        print("1 - Positivo");
    else:
        print("0 - Negativo");

def main():
    apresentar_mensagem();

main();

