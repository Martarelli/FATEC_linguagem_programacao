# 4. (Função sem retorno sem parâmetro) Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.


def conversao():
    print("Olá, tudo bem? Você informará o número de segundos e será informado em horas, minutos e segundos");
    seg = int(input("Digite a quantidade de segundos: "));
    horas = 0;
    minutos = 0;
    segundos = 0;

    if seg >= 60:
        minutos = seg // 60;
    print(minutos);


def main():
    conversao();

main();