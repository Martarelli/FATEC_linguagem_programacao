# 6. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro entre 1 e 9 e mostre a seguinte tabela de multiplicação
def tabela():
    print("Olá, tudo bem?");
    x = int(input("Digite um número inteiro: "));

    for i in range(x+1):
        for j in range(i+1):
            if j > 0:
                print(i*j, end="\t");
            else:
                j +=1;
        i += 1; 
        print("\n");

def main():
    tabela();

main();
