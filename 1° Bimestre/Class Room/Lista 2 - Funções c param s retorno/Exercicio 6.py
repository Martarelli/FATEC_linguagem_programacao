# 6. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado. Não use vetor. Aqui deverá ocorrer para as duas variáveis, PASSAGEM DE PARÂMETRO POR VALOR.
def acumulo(x, y):
    soma = 0;
    for i in range(x, y+1):
        soma += i;
        
    print("A soma dos número de %i a %i é %i" % (x, y, soma));


def main():
    x = int(input("Digite o primeiro número: "));
    y = int(input("Digite o segundo número: "));

    acumulo(x, y);


main();
