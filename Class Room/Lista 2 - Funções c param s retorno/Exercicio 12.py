# 12. Faça uma função/método para verificar uma senha, contando/apresentando quantos dígitos numéricos e quantas letras existem. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.
def conta_numeros(s):
    numeros = 0;
    for i in range(len(s)):
        if s[i].isdigit():
            numeros += 1;
    print("A senha tem %i números..."%numeros);
    
    
def main():
    s = input("Digite uma senha: ");
    conta_numeros(s);
    
main();