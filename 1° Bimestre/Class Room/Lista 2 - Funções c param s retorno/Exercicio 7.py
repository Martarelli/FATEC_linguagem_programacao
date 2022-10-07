# 7. (Função sem retorno com parâmetro) Faça uma função/método para calcular a tabuada de um número informado pelo usuário. Crie outra função que calcule a tabuada de um intervalo, por exemplo realize as taduabas do 3 ao 8. Aqui deverá ocorrer para as duas funções, PASSAGEM DE PARÂMETRO POR VALOR.
def tabuada(x):
    print("========= Tabuada do %i ========="%x)
    for i in range(1, 11):
        print("%i X %i ="%(x, i), x * i);

def tabuada_intervalo(y, z):
    for i in range(y, z+1):
        print("========= Tabuada do %i ========="%i)
        for j in range(1, 11):
            print("%i X %i ="%(i, j), j * i); 
        
    
def main():
    x = int(input("Digite o número para calc da tabuada: "));
    tabuada(x);

    y = int(input("Digite o número para calc da tabuada: "));
    z = int(input("Digite o número para calc da tabuada: "));
    tabuada_intervalo(y, z);


main();