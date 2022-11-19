# 2. Elabore uma estrutura para representar um produto (código, nome, preço). Cadastre 5 produtos, use vetor/lista. Aplique 10% de aumento no preço do produto e apresente todos os dados do preço. Não use função.

class Produto:
    codigo = 0
    nome = ""
    preco = 0.0

def main():
    prod = Produto()
    cadastros = []
    for i in range(1,6):
        prod = Produto()
        prod.codigo = int(input("Digite o codigo do produto %i: "%i))
        prod.nome = input("Digite o nome do produto %i: "%i)
        prod.preco = float(input("Digite o preço do produto %i: "%i))
        cadastros.append(prod)
    
    for i in cadastros:
        print("\n-----------------\n")
        print("CODIGO: %i\nNOME: %s\nPREÇO: %.2f\n"%(i.codigo,i.nome,i.preco))
        i.preco *= 1.1
        print("CODIGO: %i\nNOME: %s\nPREÇO APÓS AUMENTO: %.2f"%(i.codigo,i.nome,i.preco))
    
main()