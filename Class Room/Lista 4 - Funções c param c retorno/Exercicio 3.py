## 3. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário.

def aumento_salario(salario, aumento):
    x = salario *( aumento/100 + 1)
    return x

def main():
    salario = float(input("Qual o salario inicial?: "))
    aumento = int(input("Qual a % de aumento?: "))
    novo_salario = aumento_salario(salario, aumento)
    print("O salario R$%.2f, com um aumento de %i é de : R$%.2f "%(salario, aumento, novo_salario))
    
main()