# 2. (Função sem retorno sem parâmetro) Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive).

def somatorio():
    print("Olá, tudo bem? Você informará dois números e será feito a soma dos N números existentes entre eles");
    numero_um = int(input("Digite o primeiro número: "));
    numero_dois = int(input("Digite o segundo número: "));

    soma = 0;

    while numero_um <= numero_dois:
        soma += numero_um;
        numero_um += 1;

    print("O somatorio é %i"%soma);

def main():
    somatorio();

main();