# 5. (Função sem retorno sem parâmetro) Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.
def percentual():
    print("Olá, tudo bem?");
    preço_antigo = float(input("Digite um preço antigo: "));
    preço_atual = float(input("Digite um preço atual: "));

    x = (100 * preço_atual - 100 * preço_antigo) / preço_antigo;

    print("O percentual de acréscimo foi de %.2f %%"%x);


def main():
    percentual();

main();