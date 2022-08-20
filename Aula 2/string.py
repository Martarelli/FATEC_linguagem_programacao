nome = "Renan martarelli"

print("Nome do aluno " + nome)
print(10 * ".")
print(10 * nome)
print(nome.upper())
print(nome.lower())
print(nome.capitalize())

genero = "F"
if genero in "Ff":
    print("Validou")
    
print("d" not in "abc")
print("a" not in "abc")

nome2 = "        Renan             "
print(nome2.strip())

print(" ".join(nome))
print(nome.split("a"))
print(nome.split(" "))
print(nome.replace("a", "T"))

print(nome.startswith("R"))
print(nome.endswith("u"))
print(nome.count("a"))


print("renan".isalpha())
print(nome.isalpha())
print("10".isdecimal())