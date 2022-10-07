# 4. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função na main que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'.

def calc_media(p1 , p2):
    return ((p1 + p2)/ 2)

def verifica_aprovado(nota):
    if nota >= 6:
        return "APROVADO"
    else:
        return "REPROVADO"

def main():
    p1 = int(input("Nota P1: "))
    p2 = int(input("Nota P2: "))
    media = calc_media(p1, p2)
    print("O aluno obteve média %.2f e foi %s"%(media, verifica_aprovado(media)))
    
    
main()