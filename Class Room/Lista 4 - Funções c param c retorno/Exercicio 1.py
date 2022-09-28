# 1. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba por parâmetro um número e o multiplique por 2, retorne e apresente o resultado da função.

'''def multiplicar(numero):
    r = numero * 2
    # Python permite o retorno de 
    # mais que uma variável, se precisar
    return numero, r '''

def multiplicar(numero):
    r = numero * 2
    # Mais comum na programação, 
    # retorno de UMA variável
    return r 

def main():
    n = int (input('Informe o número: '))
    print(multiplicar(n)) 
    '''# ou chamada da função com mais de uma variável de retorno
    a, b = multiplicar(n)
    print('O número digitado foi: ', a)
    print('O resultado é',b)'''
     
main()