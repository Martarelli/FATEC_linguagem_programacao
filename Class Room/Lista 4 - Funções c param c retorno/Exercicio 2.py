## 2. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.

def somar(n1, n2):
    return n1 + n2

def main():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    print("O resultado é:", somar(num1, num2))
    
main()