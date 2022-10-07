# 6. (Função com retorno com parâmetro) Faça um programa contendo algumas funções:

# a) Função para construir um menu de opções para uma calculadora, como neste exemplo:

# Menu de cálculos
# 1.   Número ao quadrado
# 2.   Número ao cubo
# 3.   Raiz do número
# 4.   Raiz cúbica do número
# Qual é a opção desejada?

# b) Desenvolva uma função para cada opção de cálculo.

# Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos números do menu.

# A função da construção do menu, chamará todas as outras passando a elas o valor digitado.


def quadrado(n1):
    return n1 * n1

def cubo(n1):
    return n1 * n1 * n1

def raiz(n1):
    return n1 ** 0.5

def raiz_cubica(n1):
    return n1 ** (1/3)

def calculadora(opt):
    n1 = int(input("Digite um número: "))
    if opt == 1:
        return quadrado(n1)
    elif opt == 2:
        return cubo(n1)
    elif opt == 3:
        return raiz(n1)
    elif opt == 4:
        return raiz_cubica(n1)
    
def main():
    ligado = True
    while ligado == True:
        print("Menu de cálculos\n1.Número ao quadrado\n2.Número ao cubo\n3.Raiz do número\n4.Raiz cúbica do número\n")
        opt = int(input("Qual é a opção desejada?: "))
        if opt >= 1 and opt <=4:
            print("O resultado é: ", calculadora(opt) , "\n")
        else:
            ligado = False
            print("Volte sempre :)")
main()