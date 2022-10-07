def calcular_tabuada(numero):
    for n in range(1, 11):
        print(numero, "x", n, "=", numero * n);

def intervalo(inicio, fim):
    for n in range(inicio, fim + 1):
        calcular_tabuada(n);

def main():
    x = int(input("Informe o número: "));
    calcular_tabuada(x);
    a = int(input("Informe a primeira tabuada: "));
    b = int(input("Informe a última tabuada: "));
    intervalo(a, b);

main();