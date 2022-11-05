# 6. Elabore uma estrutura para representar um Funcionario (código, nome, endereço, salário). Para o membro endereço deve-se criar outra estrutura Endereço (logradouro, número, bairro, cidade). Utilize aninhamento de estruturas para resolver este desenvolvimento. Construa uma função para cada opçao do menu a seguir:

# Menu de opções:

#     Cadastrar funcionários
#     Visualizar todos os dados
#     Sair


class Endereco:
    rua = ""
    numero = 0
    cidade = ""
class Funcionarios:
    codigo = 0
    nome = ""
    endereco = Endereco()
    salario = 0.0

def cadastrar():
    func = Funcionarios()
    func.codigo = int(input("Codigo: "))
    func.nome = input("Nome: ")
    func.endereco.rua = input("Rua: ")
    func.endereco.numero = int(input("Numero: "))
    func.endereco.cidade = input("Cidade: ")
    func.salario = float(input("Salario: "))
    
    return func

def exibirTodos(cad):
    for i in cad:
        print("\n-----------------\n")
        print("CODIGO: %i\nNOME: %s\nRUA: %s\nNUMERO %i\nCIDADE: %s\nSALARIO: %.2f"%(i.codigo,i.nome,i.endereco.rua,i.endereco.numero,i.endereco.cidade,i.salario))
        
def main():
    op = 1
    funcionarios = []
    while op != 0:
        print("----- Menu Principal -----\n")
        print("1 - Cadastrar funcionários")
        print("2 - Visualizar todos os dados")
        print("3 - Sair")
    
        op2 = int(input("Digite a opção desejada: "))
        
        if op2 == 1:
            novo_cadastro = cadastrar()
            funcionarios.append(novo_cadastro)
            
        elif op2 == 2:
            exibirTodos(funcionarios)

        elif op2 == 3:
            print("Finalizando o programa....")
            op = 0
        else: 
            print("Opção inválida.. tente novamente...")

    
main()