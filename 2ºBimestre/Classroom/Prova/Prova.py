# 1. [6,0 pontos] Em Python crie um programa que atenda o menu a seguir. Desenvolva uma função para cada opção do menu. Utilize a criação de estruturas. Cadastrar 5 (vetor) compras e 2 (vetor) clientes.
# CLIENTES 	- 	COMPRAS
# cod_cli 	- 	cod_comp
# nome 	- 	cod_cli
# saldo_cashback 	- 	valor

# Menu de Opções

# 1 Cadastrar clientes
# 2 Mostrar todos os clientes
# 3 Cadastrar compras
# 4 Mostrar todas as compras
# 5 Mostrar o total de todas as compras realizadas por um cliente
# 6 Armazenar todas as compras em arquivo
# 7 Apresentar o conteúdo do arquivo
# 8 Gerar um gráfico
# 9 Sair

# Observaçôes:

#     Na opção 3, o valor da compra, deve ser descontado no saldo do cashback do cliente que a realizou. Por exemplo, cliente 1, tem 500 de saldo, se ele realizar uma compra de 100 reais, o saldo do cashback passará para 400.
#     Na opção 5, o usuário do sistema informará/digitará o código do cliente que quer e o sistema/programa fará uma pesquisa e calculará o total de compras do determinado cliente.
#     Na opção 6 use a função write antes da estrutura de repetição para armazenar o cabeçalho das colunas, depois dentro do laço grave todos os campos do tipo Compras como foi visto em aula, no arquivo de nome compras.csv. Use como sepador entre colunas/campos a , vírgula - usar header
#     Na opção 7 apresente todos os dados armazenados no arquivo compras.csv.
#     Na opção 8 use a coluna valor no gráfico e adote a cor orange da biblioteca Matplotlib

class Compras:
    cod_comp = 0
    cod_cli = 0
    valor = 0.0

class Clientes:
    cod_cli = 0
    nome = ""
    saldo_cashback = 0.0

def CadastrarCliente():
    cli = Clientes()
    cli.cod_cli = int(input("Digite o código do cliente: "))
    cli.nome = input("Digite o nome do cliente: ")
    cli.saldo_cashback = float(input("Saldo de cashback: R$ "))
    
    return cli

def MostrarClientes(clientes):
    print("\n--------CLIENTES CADASTRADOS--------")
    for i in clientes:
        print("\nCODIGO: %i\nNOME: %s\nSALDO CASHBACK: %.2f"%(i.cod_cli,i.nome,i.saldo_cashback))

            
def CadastrarCompra(clientes):
    comp = Compras()
    comp.cod_comp = int(input("Código da compra: "))
    comp.cod_cli = int(input("Código do cliente: "))
    comp.valor = float(input("Valor da compra: R$ "))
    for i in clientes:
        if i.cod_cli == comp.cod_cli:
            i.saldo_cashback -= comp.valor
    
    return comp, clientes

def MostrarCompras(compras):
    print("\n--------COMPRAS CADASTRADAS--------")
    for i in compras:
        print("\nCODIGO DA COMPRA: %i\nCODIGO CLIENTE: %s\nVALOR: R$ %.2f"%(i.cod_comp,i.cod_cli,i.valor))

def ComprasPorCliente(compras):
    valor_total = 0
    codigo = int(input("Informe o código do cliente: "))
    for i in compras:
        if i.cod_cli == codigo:
            valor_total += i.valor
    print("O valor total em compras do cliente cód %i é: R$ %.2f"%(codigo, valor_total))
    
def GravarComprasEmArquivo(compras):
    arquivo = open("compras_prova.csv", "w")
    arquivo.write("COD_COMP,COD_CLI,VALOR\n")
    for i in compras:
        arquivo.write("%i,%i,%.2f\n" %(i.cod_comp, i.cod_cli, i.valor))
    arquivo.close()
    
def MostrarComprasEmArquivo():
    i = 0
    arquivo = open("compras_prova.csv", "r")
    print("\n-----------COMPRAS CADASTRADAS EM ARQUIVO-----------")
    for linha in arquivo.readlines():
        comp, cli, val = linha.strip().split(',')
        if i == 0:
            print(comp,'\t',cli,'\t',val)
        else:
            print(comp,'\t\t',cli,'\t\t',val)
        i += 1
    arquivo.close()

def main():
    clientes = []
    compras = []
    op = 1
    
    while op != 0:
        print("\n--------MENU PRINCIPAL--------\n1 Cadastrar clientes\n2 Mostrar todos os clientes\n3 Cadastrar compras\n4 Mostrar todas as compras\n5 Mostrar o total de todas as compras realizadas por um cliente\n6 Armazenar todas as compras em arquivo\n7 Apresentar o conteúdo do arquivo\n8 Gerar um gráfico\n9 Sair\n")
        op = int(input("Digite a opção: "))
        if op == 1:
            novo_cliente = CadastrarCliente()
            clientes.append(novo_cliente)
            
        elif op == 2:
            MostrarClientes(clientes)
            
        elif op == 3:
            nova_compra, clientes_atualizados = CadastrarCompra(clientes)
            compras.append(nova_compra)
            clientes = clientes_atualizados
            
        elif op == 4:
            MostrarCompras(compras)
            
        elif op == 5:
            ComprasPorCliente(compras)
            
        elif op == 6:
            GravarComprasEmArquivo(compras)
            
        elif op == 7:
            MostrarComprasEmArquivo()
            
        elif op == 9:
            print("Encerrando o programa....")
            op = 0


main()