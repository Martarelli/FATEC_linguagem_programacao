# 5. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.

def aumento_salario(salario, aumento):
    x = salario *( aumento/100 + 1)
    return x

def main():
    salarios = []
    novos_salarios = []
    aumento = int(input("Qual a % de aumento?: "))
    
    for i in range(10):
        salario = float(input("Qual o salario inicial?: "))
        salarios.append(salario)
        novo_salario = aumento_salario(salario, aumento)
        novos_salarios.append(novo_salario)
        print("O salario R$%.2f, com um aumento de %i%% é de : R$%.2f "%(salarios[i], aumento, novos_salarios[i]))

    total_salarios = 0
    total_novos_salarios = 0
    for i in range(10):
        total_salarios += salarios[i]
        total_novos_salarios += novos_salarios[i]
    print("O total dos salários era R$%.2f , e com o aumentou ficou em R$%.2f"%(total_salarios, total_novos_salarios))
    diferenca = total_novos_salarios - total_salarios
    print("A diferença entre antes do aumento e depois foi de R$%.2f"%diferenca)
        
        
        
main()