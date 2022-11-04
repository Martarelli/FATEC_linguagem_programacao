# 3. Elabore uma estrutura para representar um produto (código, nome, preço). Crie uma função para cadastrar 5 produtos. Crie outra função para aplicar 10% de aumento no preço do produto e apresente, por meio de outra função, todos os dados do produtos cadastrados, após o aumento. Construa uma função para cada opção do menu a seguir:

# Menu do Sistema

#     Cadastrar
#     Reajustar
#     Visualizar
#     Sair

# Qual opção deseja?

class Produto:
    codigo = 0
    nome = ""
    preco = 0.0
def cadastrar():
    prod = Produto()
    cad = []
    for i in range(1,3):
        prod = Produto()
        prod.codigo = int(input("Digite o codigo do produto %i: "%i))
        prod.nome = input("Digite o nome do produto %i: "%i)
        prod.preco = float(input("Digite o preço do produto %i: "%i))
        cad.append(prod)
    
    return cad

def aumento(cad):
    for i in cad:
        i.preco *= 1.1
    print("Aumento executado....")
    return cad
        
def exibir(cad):
    for i in cad:
        print("\n-----------------\n")
        print("CODIGO: %i\nNOME: %s\nPREÇO: %.2f\n"%(i.codigo,i.nome,i.preco))
        
def main():
    op = 1
    produtos = []
    while op != 0:
        print("----- Menu Principal -----\n")
        print("1 - Cadastrar")
        print("2 - Reajustar")
        print("3 - Visualizar")
        print("4 - Sair")
    
        op2 = int(input("Digite a opção desejada: "))
        
        if op2 == 1:
            produtos = cadastrar()
        elif op2 == 2:
            aumento(produtos)
        elif op2 == 3:
            exibir(produtos)
        elif op2 == 4:
            print("Finalizando o programa....")
            op = 0
        else: 
            print("Opção inválida.. tente novamente...")

    
main()