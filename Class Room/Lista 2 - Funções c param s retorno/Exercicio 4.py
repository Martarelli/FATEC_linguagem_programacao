# 4. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.
def reajuste(x):
    print("O novo preço (Reajuste 9%) é", x * 1.09);
    
def main():
    x = int(input("Digite o valor do produto: "));
    reajuste(x);

main();