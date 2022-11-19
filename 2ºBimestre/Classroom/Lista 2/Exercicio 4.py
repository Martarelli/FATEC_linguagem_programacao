# 4. Baixe o arquivo futebol.txt que esta na pasta Material do aula do Teams. Leia este arquivo e o apresente. Com os dados lidos, armazene na estrutura Futebol (posicao_jogo, altura, peso, imc), calcule o IMC (Índice de Massa Corporal), armazene na estrutura e também em outro arquivo, mas agora chamado futebol_imc.txt. Apresente este novo arquivo.

# Observação: esse exercício deve ser carregado o arquivo futebol.txt, aqui no Colab, no menu (ícone pasta) do lado esquerdo, que estará disponível no Classroom.

# imc = peso / (altura ** 2)

class Futebol:
    posicao_jogo = ""
    altura = 0.0
    peso = 0.0
    imc = 0.0
    

def Imc():
    arquivo_gravacao = open("futebol_imc.txt", "w")
    arquivo = open("futebol.txt", "r")
    print("Função\t\t\tTamanho\t Peso")
    for linha in arquivo.readlines():
        func, alt, peso = linha.strip().split(',')
        print(func,'\t\t',alt,'\t',peso)
        
        f = Futebol()
       
        f.posicao_jogo = func
        f.altura = float(alt)
        f.peso = float(peso)
        f.imc = float(f.peso / (f.altura ** 2))
        arquivo_gravacao.write("%.2f\n"%(f.imc))
    arquivo.close()
    arquivo_gravacao.close()
    
    arquivo = open("futebol_imc.txt", "r")
    print("IMC")
    for linha in arquivo.readlines():
        imc = linha.strip()
        print(imc)
    arquivo.close()

def main():
    Imc()

main()