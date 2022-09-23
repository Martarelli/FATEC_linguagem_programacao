# 5. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.
def verifica():
    x = int(input("Digite um número: "))
    if x % 2 == 0:
        return "é Par"
    else:
        return "é Impar"
def main():
    verificacao = verifica()
    print("O número digitado",verificacao)
    
main()