# 1. Elabore uma estrutura para representar e armazenar 10 fornecedores (código, nome, endereco). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.

# Menu de opções:

#     Cadastrar fornecedores
#     Visualizar todos os dados
#     Sair

class Fornecedores:
    codigo = 0
    nome = ""
    end = ""

def Cadastrar(forn):
    arquivo = open("fornecedores.txt", "w")
    print("Cadastro Fornecedores...")
    for i in range(3):
        f = Fornecedores()
        f.codigo = int(input("Código: "))
        f.nome = input("Nome: ")
        f.end = input("Endereço: ")
        arquivo.write("%i; %s; %s\n" %(f.codigo, f.nome, f.end))
    arquivo.close()
    return forn

def Mostrar():
    arquivo = open("fornecedores.txt", "r")
    print("\nApresentação dos Fornecedores .........")
    print("Código\tNome\tEndereço")
    for linha in arquivo.readlines():
        cod, nome, end = linha.strip().split(';')
        print(cod,'\t',nome,'\t',end)
    arquivo.close()
    
def main():
    op = 1
    while op != 0:
        print("\n*** Cadastro Fornecedores ***")
        print("1- Cadastrar")
        print("2- Visualizar todos os dados")
        print("0- Sair")
        
        op = int(input("Digite a opção: "))
        
        if op == 1:
            fornecedores = []
            fornecedores = Cadastrar(fornecedores)
        elif op == 2:
            Mostrar()
        elif op == 0:
            continue
        else:
            print("Opção Inválida")
            
        

main()
    
