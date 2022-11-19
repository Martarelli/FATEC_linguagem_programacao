# 4. Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: nome completo, data de nascimento, telefone, endereço e série atual. Levando em conta que esta escola possui no máximo 500 alunos, como você faria para estruturar estas informações num sistema de gerenciamento para a escola? Implemente utilizando estrutura. Também use a criação de funções para cada operação. Use o menu a seguir:

# Menu de opções:

#     Cadastrar alunos
#     Consulta por nome
#     Visualizar todos os dados
#     Sair

class Alunos:
    nome = ""
    data_nasc = ""
    telefone = ""
    endereco = ""
    serie_atual = ""
    
def cadastrar():
    alu = Alunos()
    alu.nome = input("NOME COMPLETO: ")
    alu.data_nasc = input("DATA NASCIMENTO (dd/MM/yyyy): ")
    alu.telefone = input("TELEFONE: ")
    alu.endereco= input("ENDEREÇO: ")
    alu.serie_atual= input("SERIE ATUAL: ")
    
    return alu

def consultarNome(cad, nome):
    print("\nProcurando aluno(a): %s"%nome)
    encontrado = False
    for i in cad:
        if nome == i.nome:   
            print("NOME: %s\nDATA DE NASCIMENTO: %s\nTELEFONE: %s\nENDEREÇO: %s\nSERIE ATUAL: %s"%(i.nome,i.data_nasc,i.telefone,i.endereco, i.serie_atual))
            encontrado = True
            
    if encontrado == False:
        print("Aluno não encontrado........\n")

        
def exibirTodos(cad):
    for i in cad:
        print("\n-----------------\n")
        print("NOME: %s\nDATA DE NASCIMENTO: %s\nTELEFONE: %s\nENDEREÇO: %s\nSERIE ATUAL: %s"%(i.nome,i.data_nasc,i.telefone,i.endereco, i.serie_atual))
        
def main():
    op = 1
    alunos = []
    while op != 0:
        print("----- Menu Principal -----\n")
        print("1 - Cadastrar Aluno")
        print("2 - Consulta por nome")
        print("3 - Visualizar todos os dados")
        print("4 - Sair")
    
        op2 = int(input("Digite a opção desejada: "))
        
        if op2 == 1:
            novo_cadastro = cadastrar()
            alunos.append(novo_cadastro)
        elif op2 == 2:
            nome_procurado = input("Digite o NOME COMPLETO que deseja procurar: ")
            consultarNome(alunos, nome_procurado)
        elif op2 == 3:
            exibirTodos(alunos)
        elif op2 == 4:
            print("Finalizando o programa....")
            op = 0
        else: 
            print("Opção inválida.. tente novamente...")

    
main()