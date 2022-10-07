# 7. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:

# a) Função para construir um menu de opções para uma calculadora:

# *** Minha Calculadora ***
# Digite um número.....: 
# Digite outro número..: 
#     + Soma dois números
#     - Subtrai dois números
#     * Multiplica dois números
#     / Divide dois números
# Qual opção deseja? 

# b) Desenvolva uma função para cada opção de cálculo, mas estas não terão retorno.

# Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos caracteres do menu.

# A função da construção do menu, chamará todas as outras passando a elas os valores digitados.

def soma(n1, n2):
    print("\nResultado de %i + %i = %i\n"%(n1, n2, n1+n2))

def subtracao(n1, n2):
    print("\nResultado de %i - %i = %i\n"%(n1, n2, n1-n2))

def divisao(n1, n2):
    print("\nResultado de %i / %i = %.2f\n"%(n1, n2, n1/n2))

def multiplicacao(n1, n2):
    print("\nResultado de %i * %i = %i\n"%(n1, n2, n1*n2))

def main():
    ligado = True
    while ligado:
        print("\t*** Minha Calculadora ***")
        n1 = int(input("Digite um número.....: ")) 
        n2 = int(input("Digite outro número..: ")) 
        print("+ Soma dois números\n- Subtrai dois números\n* Multiplica dois números\n/ Divide dois números\n")
        op = input("Qual opção deseja?: ")
        
        if op == "+":
            soma(n1, n2)
        elif op == "-":
            subtracao(n1, n2)
        elif op == "/":
            divisao(n1, n2)
        elif op == "*":
            multiplicacao(n1, n2)
        else:
            print("Desligando a calculadora.....")
            ligado = False

main()