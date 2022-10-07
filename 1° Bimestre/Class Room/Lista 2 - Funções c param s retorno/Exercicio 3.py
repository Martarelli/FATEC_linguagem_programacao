# 3. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.
def sub(x, y):
    print("o número %i - %i é igual:"%(x, y), x - y);
def main():
    x = int(input("Digite um número: "));
    y = int(input("Digite outro número: "));
    sub(x, y)

main();