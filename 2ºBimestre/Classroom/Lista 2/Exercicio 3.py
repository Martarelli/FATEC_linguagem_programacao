# 3. Elabore uma estrutura para representar e armazenar 10 alunos (matricula, nome, telefone). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.

# Menu de opções:

#     Cadastrar alunos
#     Visualizar todos os dados
#     Sair

class Alunos:
    matricula = 0
    nome = ""
    telefone = ""
    
def Cadastrar(alu):
    arquivo = open("alunos.txt", "w")
    print("Cadastro Produtos...")
    for i in range(3):
        f = Alunos()
        f.matricula = int(input("Matricula: "))
        f.nome = input("Nome: ")
        f.telefone = input("Telefone: ")
        arquivo.write("%i; %s; %s\n" %(f.matricula, f.nome, f.telefone))
    arquivo.close()
    return alu

def Mostrar():
    arquivo = open("alunos.txt", "r")
    print("\nApresentação dos Alunos .........")
    print("Matricula\tNome\tTelefone")
    for linha in arquivo.readlines():
        mat, nome, tel = linha.strip().split(';')
        print(mat,'\t\t',nome,'\t',tel)
    arquivo.close()
    
def main():
    op = 1
    while op != 0:
        print("\n*** Cadastro de Alunos ***")
        print("1- Cadastrar")
        print("2- Visualizar todos os dados")
        print("0- Sair")
        
        op = int(input("Digite a opção: "))
        
        if op == 1:
            alunos = []
            alunos = Cadastrar(alunos)
        elif op == 2:
            Mostrar()
        elif op == 0:
            continue
        else:
            print("Opção Inválida")
main()
    