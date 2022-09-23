# 4. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área, area = lado².

def area():
    l = int(input("Qual tamanho do lado do quadrado?: "))
    area = l ** 2
    return area

def main():
    a = area()
    print("A area do quadrado é  %.2f"%a)    
main()