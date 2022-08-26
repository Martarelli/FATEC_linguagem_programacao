# 3. (Função sem retorno sem parâmetro) Faça uma função/método que receba três números inteiros a, b, c que sejam divisíveis por a. Os valores b e c representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. Não pode usar vetor e função pronta da linguagem Python.

def numeros_divisiveis():
    print("Olá, tudo bem? Você informará três números e será mostrado quais numeros do intervalo entre o segundo e terceiro número informado é divisivel pelo primeiro número");
    numero_um = int(input("Digite o primeiro número: "));
    numero_dois = int(input("Digite o segundo número: "));
    numero_tres = int(input("Digite o terceiro número: "));
    soma = 0;
    while numero_dois <= numero_tres:
        if numero_dois % numero_um == 0:
            print("O número %i é divisivel pelo número %i"%(numero_dois, numero_um));
            soma += 1;
        numero_dois += 1;
    
    print("%i número foram divisiveis por %i"%(soma, numero_um));

def main():
    numeros_divisiveis();

main();
