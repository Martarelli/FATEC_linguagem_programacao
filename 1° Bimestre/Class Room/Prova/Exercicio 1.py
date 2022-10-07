# 1. [2,00 pontos] O recebimento de produtos comprados por um hipermercado, é distribuído de forma igualitaria, 8 caixas de produtos em cada palete, para serem armazenados no depósito. O resto das caixas são colocadas nas gondolas.

# Crie uma função/método (sem parâmetro) utilizando a linguagem Python, que calcule e apresente a quantidade de paletes necessários. Retorne o resto da quantidade de caixas.

# Implemente outra função/método (com parâmetro) que calcule e apresente, do resto das caixas a quantidade de produtos que serão colocados nas gondolas. Cada caixa tem 12 produtos.
# Utilize a função main() para a chamada das funções.

# Lembrete, na função que tem parâmetro, este, neste caso, na programação, é chamado de PASSAGEM DE PARÂMETRO POR VALOR.

# Curiosidade: Palete é um estrado de madeira, metal ou plástico que é utilizado para empilhar ou transportar materiais por meio de empilhadeiras.
def paletes():
    qtd_recebida = int(input("Qual a quantidade de produtos recebidos?: "))
    qtd_paletes = qtd_recebida // 8
    resto = qtd_recebida - (qtd_paletes * 8)
    print("Quantidade de paletes necessários: %i - Caixas restantes %i"%(qtd_paletes, resto))
    
    return resto

def produtos_gondula(cx):
    qtd_produtos = cx * 12
    print("Serão colocados %i produtos nas gondulas"%qtd_produtos)
    
def main():
    resto_paletes = paletes()
    produtos_gondula(resto_paletes)    
    
main()