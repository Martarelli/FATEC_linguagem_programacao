# 5. Faça um programa que realize o cadastro de contas bancarias com as seguintes informações: numero da conta, nome do titular e saldo. O banco permitirá o cadastramento de 15 contas. Crie uma função para cada opção do menu a seguir. Utilize a estrutura na passagem de parâmetro:

# Menu de opções:

#     Cadastrar contas
#     Visualizar todas as contas
#     Consultar por nome
#     Alterar nome e/ou saldo de um número de conta
#     Excluir a conta com menor saldo
#     Sair

# Observação:

#     No item de menu 4. Alterar nome e/ou saldo de um número de conta, entenda que apenas pode ser alterado o nome e o saldo depois que você pesquisar pelo número da conta.
#     No item 5 do menu, encontre o menor saldo dentre todos cadastrados, depois exclua esta ÚNICA conta.. O assunto de excluir algo de um vetor foi dado na disciplina de Algoritmo.

class Contas:
    numero = ""
    nome = ""
    saldo = ""
    
def cadastrar():
    conta = Contas()

    conta.numero = int(input("NUMERO DA CONTA: "))
    conta.nome = input("NOME: ")
    conta.saldo = float(input("SALDO: "))
    
    return conta

def consultarNome(cad, nome):
    print("\nProcurando cliente: %s"%nome)
    encontrado = False
    for i in cad:
        if nome == i.nome:   
            print("NUMERO CONTA: %i\nNOME: %s\nSALDO: %.2f"%(i.numero,i.nome,i.saldo))
            encontrado = True
            
    if encontrado == False:
        print("Cliente não encontrado........\n")

def alterarConta(cad, numero):
    print("\nNúmero da conta pesquisada: %i"%numero)
    encontrado = False
    for i in cad:
        if numero == i.numero:   
            print("NUMERO CONTA: %i\nNOME: %s\nSALDO: %.2f"%(i.numero,i.nome,i.saldo))
            encontrado = True
            novo_nome = input("Digite o novo nome: ")
            if novo_nome != "":
                i.nome = novo_nome
            novo_saldo = input("Digite o novo saldo: ")
            if novo_saldo != "":
                i.saldo = float(novo_saldo)
            
    if encontrado == False:
        print("Conta não encontrado........\n")
    
    return cad
        
def exibirTodos(cad):
    for i in cad:
        print("\n-----------------\n")
        print("NUMERO CONTA: %i\nNOME: %s\nSALDO: %.2f"%(i.numero,i.nome,i.saldo))
        
def excluirMenorSaldo(cad):
    menor_saldo = -1
    menor_saldo_indice = 0
    for i in range(len(cad)):
        if menor_saldo == -1:
            menor_saldo = cad[i].saldo
            menor_saldo_indice = i
        elif cad[i].saldo < menor_saldo:
            menor_saldo = cad[i].saldo
            menor_saldo_indice = i
    print("NUMERO CONTA: %i\nNOME: %s\nSALDO: %.2f"%(cad[menor_saldo_indice].numero,cad[menor_saldo_indice].nome,cad[menor_saldo_indice].saldo))
    opcao = input("DESEJA EXCLUIR A CONTA SELECIONADA?????? S / N : ").upper()
    if opcao == "S":
        cad.pop(menor_saldo_indice)
        print("Conta EXCLUIDA com sucesso.....")
    elif opcao == "N":
        print("A conta NÃO foi excluida.....")
    else:
        print("OPCÃO INVALIDA..... A conta NÃO foi excluida.....")
        
    return cad  
    
def main():
    op = 1
    clientes = []
    while op != 0:
        print("----- Menu Principal -----\n")
        print("1 - Cadastrar conta")
        print("2 - Consultar por nome")
        print("3 - Visualizar todas as contas")
        print("4 - Alterar nome e/ou saldo de um número de conta")
        print("5 - Excluir a conta com menor saldo")
        print("6 - Sair")
    
        op2 = int(input("Digite a opção desejada: "))
        
        if op2 == 1:
            novo_cadastro = cadastrar()
            clientes.append(novo_cadastro)
        elif op2 == 2:
            nome_procurado = input("Digite o NOME COMPLETO que deseja procurar: ")
            consultarNome(clientes, nome_procurado)
        elif op2 == 3:
            exibirTodos(clientes)
        elif op2 == 4:
            conta_procura = int(input("Número da conta para alteração: "))
            clientes = alterarConta(clientes, conta_procura)
        elif op2 == 5:
            clientes = excluirMenorSaldo(clientes)
        elif op2 == 6:
            print("Finalizando o programa....")
            op = 0
        else: 
            print("Opção inválida.. tente novamente...")

    
main()