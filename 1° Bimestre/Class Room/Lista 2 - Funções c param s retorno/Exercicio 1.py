# 1. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado. Este é um exemplo de PASSAGEM DE PARÂMETRO POR VALOR.
def mult(x):
    print("O número %i X 2 é: "%x,(x * 2));

def main():
    n = int(input("Digite um número: "))
    mult(n);

main();