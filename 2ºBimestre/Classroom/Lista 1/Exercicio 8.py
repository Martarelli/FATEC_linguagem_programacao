# 8. Elabore duas estruturas, como é apresentado a seguir:
# CLIENTE 	DOCUMENTOS
# cod_cli 	num_doc
# nome 	cod_cli
# fone 	dia_venc
# 	dia_pag
# 	valor
# 	juros

#     Sabe-se que um documento só pode ser cadastrado para um cliente que já exista.

#     Considere que podem existir, no máximo, 15 clientes e 30 documentos. Crie um vetor para clientes e outro para documentos.

#     Crie um menu para a realização de cada uma das operações especificadas a seguir:

# ** SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS **

#     Cadastrar clientes

#     Relatório de clientes

#     Cadastrar documentos

#     Relatório de documentos

#     Excluir clientes sem documentos

#     Excluir documentos individuais pelo número

#     Excluir documentos por cliente

#     Excluir documentos por período

#     Alterar as informações dos clientes

#     Mostrar o total de documentos de determinado cliente

#     Sair

# Qual opção deseja?

# .................................................................................................

# Para cada item do menu, desenvolva uma função.

# A seguir são apresentados os detalhes de implementação de cada opção do menu:

#     Cadastrar clientes — não pode existir mais que um cliente com o mesmo código.

#     Relatório de clientes - listar todos os clientes cadastrados.

#     Cadastrar documentos — ao cadastrar um documento, se o dia de pagamento for maior que o dia de vencimento, calcular o campo ‘juros’ do registro documentos (5% sobre o valor original do documento).

#     Relatório de documentos - listar todos os documentos cadastrados.

#     Excluir clientes — um cliente só poderá ser excluído se não existir nenhum documento associado a ele.

#     Excluir documentos individuais — por meio de seu número. Caso o documento não exista, o programa deverá mostrar a mensagem "Documento não encontrado".

#     Excluir documentos por cliente — o programa deverá informar o código do cliente e excluir todos os seus documentos. Caso o cliente não exista, deverá mostrar a mensagem "Cliente não encontrado".

#     Excluir documentos por período — o programa deverá informar o dia inicial e o dia final e excluir todos os documentos que possuam data de vencimento nesse período.

#     Alterar as informações sobre os clientes — só NÃO altere o código do cliente.

#     Mostrar o total de documentos de determinado cliente.
class Clientes:
    cod_cli = 0
    nome = ""
    fone = ""
    
class Documentos:
    num_doc = 0
    cod_cli = 0
    dia_venc = ""
    dia_pag = ""
    valor = 0.0
    juros = 0.0
    

def main():
    documentos = []
    clientes = []
    op = 1
    
    while(op != 0):
        print("1 - Cadastrar clientes")
        print("2 - Relatório de clientes")
        print("3 - Cadastrar documentos")
        print("4 - Relatório de documentos")
        print("5 - Excluir clientes sem documentos")
        print("6 - Excluir documentos individuais pelo número")
        print("7 - Excluir documentos por cliente")
        print("8 - Excluir documentos por período")
        print("9 - Alterar as informações dos clientes")
        print("10 - Mostrar o total de documentos de determinado cliente")
        print("0 - Sair")
        
        op = int(input("Digite a opção desejada: "))
    
        if op == 1:
            if len(clientes) < 2:
                cliente = Clientes()
                cliente.cod_cli = int(input("Código do cliente: "))
                cliente.nome = input("Nome do cliente: ")
                cliente.fone = input("Telefone: ")
                clientes.append(cliente)
            else:
                print("\nNão é possível cadastrar, o cadastro está cheio...\n")
        elif op == 2:
            for i in clientes:
                print("\n------------------------------")
                print("Codigo: ", i.cod_cli)
                print("Nome: ", i.nome)
                print("Telefone: ", i.fone)
                print("------------------------------")
            print("")
        elif op == 0:
            pass

    
main()