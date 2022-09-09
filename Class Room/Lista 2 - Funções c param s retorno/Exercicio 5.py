# 5. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada (digitada) pelo usuário. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.
def reajuste(x, y):
    novo_valor = x + x * (y / 100);
    print("O valor com o acréscimo é:",  novo_valor);


def main():
    x = int(input("Digite o valor do produto: "))
    y = int(input("Digite o valor % de reajuste: "))

    reajuste(x, y)


main()
