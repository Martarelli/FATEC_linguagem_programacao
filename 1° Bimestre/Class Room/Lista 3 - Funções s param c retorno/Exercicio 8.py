# 8. (Função com retorno sem parâmetro) Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é igual a soma de seus divisores (exceto ele mesmo).
# Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito. Não use função pronta.
# 1º número perfeito: 6
# 2º número perfeito: 28
# 3º número perfeito: 496
def num_perfeito():
    A = []
    num_atual = 1
    while len(A) < 3:
        divisores = []
        for i in range(1, num_atual):
            if num_atual % i == 0:
                divisores.append(i)

        soma = 0
        for j in range(len(divisores)):
            soma += divisores[j]

        if soma == num_atual:
            A.append(num_atual)
        
        num_atual += 1   
        
    return A     

def main():
    print(num_perfeito())
    
main()