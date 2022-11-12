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
    dia_venc = 0
    dia_pag = 0
    valor = 0.0
    juros = 0.0
    
def ExcluirSemDocumento(clientes, documentos):
    clientes_com_cadastro = []
    for i in clientes:
        for j in documentos:
            if i.cod_cli == j.cod_cli and i not in clientes_com_cadastro:
                clientes_com_cadastro.append(i)
                continue
         
    return clientes_com_cadastro

def ExcluirDocumentoPorNumero(documentos, doc_excluir):
    doc = []
    excluido = 0
    for i in documentos:
        if i.num_doc == doc_excluir:
            excluido = 1
        else:
            doc.append(i)
            
    if excluido == 1:
        print("Documento Excluido...")
        return doc
    else:
        print("Documento não encontrado...")
        return documentos
            
def ExcluirDocumentosDeCliente(documentos, cod_cli):
    doc = []
    for i in documentos:
        if i.cod_cli == cod_cli:
            excluido = 1
        else:
            doc.append(i)
            
    if excluido == 1:
        print("Exclusão concluida...")
        return doc
    else:
        print("Cliente não encontrado...")
        return documentos

def ExcluirPorPeriodo(documentos, dia_inicial, dia_final):
    doc = []
    for i in documentos:
        if i.dia_venc >= dia_inicial and i.dia_venc <= dia_final:
            excluido = 1
        else:
            doc.append(i)
            
    if excluido == 1:
        print("Exclusão concluida...")
        return doc
    else:
        print("Nenhum documento encontrado no periodo...")
        return documentos
    
def AlterarCliente(clientes, codigo_cliente):
    cli = []
    for i in clientes:
        if i.cod_cli == codigo_cliente:
            i.nome = input("Nome do cliente: ")
            i.fone = input("Telefone: ")
            doc.append(i)
            alterado = 1
        else:
            doc.append(i)
            
    if alterado == 1:
        print("Alteração concluida...")
        return doc
    else:
        print("Cliente não encontrado...")
        return documentos
    
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
            existe = True
            if len(clientes) < 2:
                cliente = Clientes()
                cliente.cod_cli = int(input("Código do cliente: "))
                for i in clientes:
                    if cliente.cod_cli == i.cod_cli:
                        existe = False
                if existe:
                    cliente.nome = input("Nome do cliente: ")
                    cliente.fone = input("Telefone: ")
                    clientes.append(cliente)
                    existe = True
                else:
                    print("Código já cadastrado...")
            else:
                print("\nNão é possível cadastrar, o cadastro está cheio...\n")
        elif op == 2:
            if len(clientes) != 0:
                for i in clientes:
                    print("\n------------------------------")
                    print("Codigo: ", i.cod_cli)
                    print("Nome: ", i.nome)
                    print("Telefone: ", i.fone)
                    print("------------------------------")
                print("")
        elif op == 3:
            if len(documentos) < 4:
                existe = False
                doc = Documentos()
                doc.cod_cli = int(input("Código do cliente: "))
                
                for i in clientes:
                    if doc.cod_cli == i.cod_cli:
                        existe = True

                if existe:
                    doc.num_doc = int(input("Número do Documento: "))
                    doc.dia_venc = int(input("Dia do vencimento: "))
                    doc.dia_pag = int(input("Dia do pagamento: "))
                    doc.valor = float(input("Valor: R$"))
                    if doc.dia_pag > doc.dia_venc:
                        doc.juros = doc.valor * 0.05
                    else:
                        doc.juros = 0
                    documentos.append(doc)
                    existe = False
                else:
                    print("Cliente não cadastrado...")
                
            else:
                print("\nNão é possível cadastrar, o cadastro está cheio...\n")
        elif op == 4:
            for i in documentos:
                print("\n------------------------------")
                print("Codigo do Cliente: ", i.cod_cli)
                print("Codigo do Documento: ", i.num_doc)
                print("Dia Vencimento: ", i.dia_venc)
                print("Dia Pagamento: ", i.dia_pag)
                print("Valor: R$", i.valor)
                print("Juros: R$", i.juros)
                print("------------------------------")
            print("")
        elif op == 5:
            clientes = ExcluirSemDocumento(clientes, documentos)
            
        elif op == 6:
            doc_excluir = int(input("Número do documento: "))
            documentos = ExcluirDocumentoPorNumero(documentos, doc_excluir)
            
        elif op == 7:
            docs_cliente_excluir = int(input("Código do cliente: "))
            documentos = ExcluirDocumentosDeCliente(documentos, docs_cliente_excluir)
                    
        elif op == 8:
            dia_inicial = int(input("Inicio do periodo: "))
            dia_final = int(input("Final do periodo: "))
            documentos = ExcluirPorPeriodo(documentos, dia_inicial, dia_final)
        
        elif op == 9:
            codigo_cliente_alterar = int(input("Código do cliente: "))
            clientes = AlterarCliente(clientes, codigo_cliente_alterar)
                    
        elif op == 0:
            continue

    
main()