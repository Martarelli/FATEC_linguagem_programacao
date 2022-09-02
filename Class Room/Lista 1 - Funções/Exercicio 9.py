# 9. (Função sem retorno sem parâmetro) Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles. Não pode usar vetor e função pronta da linguagem Python.

def maior_menor():
    maior = int(input("Digite um número: "));
    menor = maior;
    for i in range(4):
        i = int(input("Digite um número: "))
        if i > maior:
            maior = i;
        elif i < menor:
            menor = i;
    print("O maior número informado foi: %i, e o menor número foi %i."%(maior,menor))

def main():
    maior_menor();

main();