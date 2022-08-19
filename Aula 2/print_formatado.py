nome = "Ana"
idade = 25
p1= 5.3478
p2= 7.5599
media = (p1 + p2) / 2


print("%s tem %i anos de idade e obteve nota média de %f" %(nome, idade,media))
print("%s tem %i anos de idade e obteve nota média de %.2f" %(nome, idade,media))
print("%s tem %5i anos de idade e obteve nota média de %.2f" %(nome, idade,media))
print("%s tem %05i anos de idade e obteve nota média de %.2f" %(nome, idade,media))
print("%s tem %-5i anos de idade e obteve nota média de %.2f" %(nome, idade,media))
print("%-12s tem %i anos de idade e obteve nota média de %.2f" %(nome, idade,media))
print("%12s tem %i anos de idade e obteve nota média de %.2f" %(nome, idade,media))
print("%12s tem %i anos de idade e obteve nota média de %10.2f" %(nome, idade,media))