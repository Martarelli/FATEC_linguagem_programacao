# 7. Elabore uma estrutura para representar um Produto (código, nome, data_fabricacao, data_validade, preço). Para o membro data_fabricacao e data_validade, deve-se criar outra estrutura Data (dia, mês, ano). Utilize aninhamento de estruturas para resolver este desenvolvimento. Construa uma função para cada opçao do menu a seguir:

# Menu de opções:

#     Cadastrar produtos
#     Visualizar todos os dados
#     Sair


class Data:
    dia = 0
    mes = 0
    ano = 0
    
class Produtos:
    codigo = 0
    nome = ""
    data_fabricacao = Data()
    data_validade = Data()
    preco = 0.0

def cadastrar():
    prod = Produtos()
    prod.codigo = int(input("Codigo: "))
    prod.nome = input("Nome: ")
    prod.data_fabricacao.dia = int(input("Dia Fabricação: "))
    prod.data_fabricacao.mes = int(input("Mês Fabricação: "))
    prod.data_fabricacao.ano = int(input("Ano Fabricação: "))
    prod.data_validade.dia = int(input("Dia Validade: "))
    prod.data_validade.mes = int(input("Mês Validade: "))
    prod.data_validade.ano = int(input("Ano Validade: "))
    prod.preco = float(input("Preço: "))
    
    return prod

def exibirTodos(cad):
    for i in cad:
        print("\n-----------------\n")
        print("CODIGO: %i\nNOME: %s\nDATA FABRICAÇÃO: %i/%i/%i\nDATA VALIDADE: %i/%i/%i\nPREÇO: %.2f"%(i.codigo,i.nome,i.data_fabricacao.dia,i.data_fabricacao.mes,i.data_fabricacao.ano,i.data_validade.dia,i.data_validade.mes,i.data_validade.ano,i.preco))
        
def main():
    op = 1
    produtos = []
    while op != 0:
        print("----- Menu Principal -----\n")
        print("1 - Cadastrar produtos")
        print("2 - Visualizar todos os dados")
        print("3 - Sair")
    
        op2 = int(input("Digite a opção desejada: "))
        
        if op2 == 1:
            novo_cadastro = cadastrar()
            produtos.append(novo_cadastro)
            
        elif op2 == 2:
            exibirTodos(produtos)

        elif op2 == 3:
            print("Finalizando o programa....")
            op = 0
        else: 
            print("Opção inválida.. tente novamente...")

    
main()