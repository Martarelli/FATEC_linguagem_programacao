# 3. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área A = (base x altura)/2.
def area():
    b = int(input("Qual tamanho da base do triangulo?: "))
    h = int(input("Qual altura do triangulo?: "))
    area = (b * h)/2
    return area

def main():
    a = area()
    print("A área do triangulo é: %.2f"%a)
    
main()