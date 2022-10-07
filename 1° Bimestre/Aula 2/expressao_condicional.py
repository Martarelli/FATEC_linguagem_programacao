#CRIE UM PROGRAMA QUE CALCULE A MEDIA DE DUAS PROVAS E APRESENTE SE O ALUNO ESTÁ APROVADO OU REPROVADO
p1 = float(input("Digite a nota da p1: "))
p2 = float(input("Digite a nota da p2: "))
media = (p1+p2)/2

print("A média foi de %.2f"%media)
print("APROVADO" if media >= 6 else "REPROVADO")