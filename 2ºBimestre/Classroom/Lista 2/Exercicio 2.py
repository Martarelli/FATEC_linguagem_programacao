# 2. Elabore uma estrutura para representar e armazenar 10 produtos (código, nome, preço). Utilize os recursos de arquivo para armazenar estes dados permanentemente. O nome do arquivo deve ser o mesmo da estrutura. Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.

# Menu de opções:

#     Cadastrar produtos
#     Visualizar todos os dados
#     Sair
class Produtos:
    codigo = 0
    nome = ""
    preco = 0.0
    
def Cadastrar(pd):
    arquivo = open("produtos.txt", "w")
    print("Cadastro Produtos...")
    for i in range(3):
        f = Produtos()
        f.codigo = int(input("Código: "))
        f.nome = input("Nome: ")
        f.preco = int(input("Preço: R$"))
        arquivo.write("%i; %s; %s\n" %(f.codigo, f.nome, f.preco))
    arquivo.close()
    return pd

def Mostrar():
    arquivo = open("produtos.txt", "r")
    print("\nApresentação dos Produtos .........")
    print("Código\tNome\tPreço(R$)")
    for linha in arquivo.readlines():
        cod, nome, preco = linha.strip().split(';')
        print(cod,'\t',nome,'\t',preco)
    arquivo.close()
    
def main():
    op = 1
    while op != 0:
        print("\n*** Cadastro de Produtos ***")
        print("1- Cadastrar")
        print("2- Visualizar todos os dados")
        print("0- Sair")
        
        op = int(input("Digite a opção: "))
        
        if op == 1:
            produtos = []
            produtos = Cadastrar(produtos)
        elif op == 2:
            Mostrar()
        elif op == 0:
            continue
        else:
            print("Opção Inválida")
main()
    