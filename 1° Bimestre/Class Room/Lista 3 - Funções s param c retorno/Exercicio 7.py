# 7. (Função com retorno sem parâmetro) Faça uma função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, que armazenará o fatorial de cada elemento de A. Não use função pronta de cálculo de fatorial. Retorne/apresente o vetor B.

def fatorial():
    A = []
    B = []
    for i in range(5):
        A.append(int(input("Digite um número: ")))

    for i in A:
        fact = 1
        for j in range(1,i + 1):
            fact = fact * j
        B.append(fact)
    return B

def main():
    x = fatorial()
    print(x)
main()