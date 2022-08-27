# 4. (Função sem retorno sem parâmetro) Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.


def conversao():
    print("Olá, tudo bem? Você informará o número de segundos e será informado em horas, minutos e segundos");
    segundos = int(input("Digite a quantidade de segundos: "));

    # segundos = segundos % (24 * 3600) ;

    horas = segundos // 3600;
    segundos %= 3600;
    minutos = segundos // 60;
    segundos %= 60;

    print("%.0f:%02.0f:%02.0f"%(horas, minutos, segundos))

def main():
    conversao();

main();