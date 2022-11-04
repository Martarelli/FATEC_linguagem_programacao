# 1. Elabore uma estrutura para representar um produto (código, nome, preço). Aplique 10% de aumento no preço do produto e apresente. Não use função.

class Produto:
    codigo = 0
    nome = ""
    preco = 0.0

def main():
    prod = Produto()
    prod.codigo = 999
    prod.nome = "Produto zica"
    prod.preco = 20
    print("CODIGO: %i\nNOME: %s\nPREÇO: %.2f\n"%(prod.codigo,prod.nome,prod.preco))
    prod.preco *= 1.1
    print("CODIGO: %i\nNOME: %s\nPREÇO APÓS AUMENTO: %.2f"%(prod.codigo,prod.nome,prod.preco))
    
main()