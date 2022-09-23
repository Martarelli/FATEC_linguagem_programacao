# 2. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando.
def subtracao():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    return n1-n2

def main():
    x = subtracao()
    print("A subtração é:", x)
    
main()
