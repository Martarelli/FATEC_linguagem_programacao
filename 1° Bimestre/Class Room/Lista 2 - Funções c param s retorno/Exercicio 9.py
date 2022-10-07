# 9. (Função sem retorno com parâmetro) Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar.
def par_ou_impar(p1):
    if p1 % 2 == 0:
        print("É Par");
    else: 
        print("É Impar")
        
def valor():
    p1 = int(input("Digite um número: "));
    par_ou_impar(p1);
    
def main():
    valor();
    
main();