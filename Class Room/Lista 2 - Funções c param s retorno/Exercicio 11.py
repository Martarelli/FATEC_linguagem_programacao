# 11. (Função sem retorno com parâmetro) Faça uma função/método para verificar e contar quantas letras a tem numa frase. Não use NENHUMA função pronta da linguagem Python. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.
def conta_letra(word):
    letras_a = 0;
    for i in range(len(word)):
        if word[i] == "a":
            letras_a += 1;
    
    print("a palavra %s tem %i letras A..."%(word.upper(),letras_a)) ;     

def main():
    s = input("Digite uma palavra: ");
    conta_letra(s);
    
main();