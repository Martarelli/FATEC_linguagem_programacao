# 10. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo:
# S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
# Observvação: Não pode usar vetor e função pronta da linguagem Python.
def calculo():
    N = int(input("Digite um número: "));
    if N > 0:
        S = 1;
        for i in range(1, N + 1):
            fat = 1
            for j in range(1, i + 1):
                fat = fat * j;
            S += (1 / fat);
        print("O valor S é: %.5f"%(S))
    else:
        print("O número informado não pode ser igual ou menor que 0!!!")
        calculo();

def main():
    calculo();

main();