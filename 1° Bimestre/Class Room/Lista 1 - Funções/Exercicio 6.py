# 6. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro entre 1 e 9 e mostre a seguinte tabela de multiplicação
def tabela():
    print("Olá, tudo bem?");
    x = int(input("Digite um número inteiro: "));

    for i in range(1,x+1):
        for j in range(1,i+1):
            print(i*j, end="\t");
        print();

def main():
    tabela();

main();
