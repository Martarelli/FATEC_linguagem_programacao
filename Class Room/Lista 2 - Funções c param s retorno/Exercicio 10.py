# 10. (Função sem retorno com parâmetro) Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.
def verifica_nome(s):
    nome = s.upper()
    if nome == "ANA":
        print(True)
    else:
        print(False)
    
def main():
    s = input("Digite o nome: ");
    verifica_nome(s);
main();