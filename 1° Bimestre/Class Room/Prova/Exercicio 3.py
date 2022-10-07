# 3. [2,50 pontos] O IPVA (Imposto sobre a Propriedade de Veículos Automotores) no estado de São Paulo, possui valor de alíquota de imposto variável de acordo com o tipo de veículo automotor.

# Crie uma função que receba como parâmetro o valor do veículo e uma letra, F, ou E, ou C, ou M, ou O, ou A, a função retornará a porcentagem para auxiliar o cálculo do item b). Para esta verificação, siga a instrução do governo para cada tipo de veículo automotor: Flex => 4%, Elétrico => 3%, Caminhonete => 2%, Moto => 2%, Onibus => 2%, cAminhao 1.5%.

# Dependendo do ano de fabricação, pode ocorrer isenção de IPVA, ou seja, não é pago nada, referente a este imposto. O estado de São Paulo concede isenção a partir de 20 anos de fabricação.

# Atendendo a 10 proprietários de automóveis, a partir dos anos de fabricação, tipo de veículo automotor e dos valores dos carros, crie um programa que atenda cada item a seguir, na main() calcule e apresente:

# a) Quantidade de veículos automotores isentos.

# b) Valor do IPVA de veículo automotor, use a função requerida.

# c) Média de valores dos veículos automotores.

# d) Total dos IPVAs pagos.
# Não use vetor/matriz.

# Curiosidade: O valor do veículo geralmente é avaliado pela tabela FIPE (Fundação Instituto de Pesquisas Econômicas).
def porc_imposto(tipo):
    if tipo == "f":
        return 0.04
    elif tipo == "e":
        return 0.03
    elif tipo == "c":
        return 0.02
    elif tipo == "m":
        return 0.02
    elif tipo == "o":
        return 0.02
    elif tipo == "a":
        return 0.015

    
def main():
    tot_isentos = 0
    tot_valor = 0
    tot_IPVA = 0
    media_valor = 0
    tot_veic = 10
    
    for i in range(tot_veic):
        valor_veic = float(input("Digite o valor do veiculo: "))
        tot_valor += valor_veic
        print("Tipo de veiculo:\nF - Flex\nE - Eletrico\nC - Caminhote\nM - Moto\nO - Onibus\nA - Caminhão")
        tipo_veic = input("Qual tipo do veiculo?: ").lower()
        ano_veic = int(input("Ano de fabricação: "))
        porcentagem_imposto = porc_imposto(tipo_veic)
        imposto_devido = valor_veic * porcentagem_imposto
        
        if ano_veic >= 2002:            
            tot_IPVA += imposto_devido 
            print("Valor do IPVA = R$%.2f"%imposto_devido)
        else:
            print("Veiculo Isento")
            tot_isentos += 1
            
    print("Total de Veiculos isentos: %i"%tot_isentos)
    print("Media do valor dos veiculos: %.2f"%(tot_valor/tot_veic))
    print("Total de impostos arrecadados: %.2f"%tot_IPVA)
  
main()