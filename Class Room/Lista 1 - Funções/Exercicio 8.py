# 8. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.

def duracao_jogo():
    
    hora_inicio = int(input("Informe a hora de inicio do jogo: "));
    minuto_inicio = int(input("Informe os minutos de inicio do jogo: "));
    hora_termino = int(input("Informe a hora de termino do jogo: "));
    minuto_termino = int(input("Informe os minutos do termino do jogo: "));

    if hora_inicio <= hora_termino and minuto_inicio < minuto_termino:
        hora_min = (hora_termino - hora_inicio) * 60;
        minutos = minuto_termino - minuto_inicio;
        duracao = hora_min + minutos;
        print("A duração do jogo foi de %i minutos"%duracao);
    elif hora_inicio <= hora_termino and minuto_inicio >= minuto_termino:
        hora_min = (hora_termino - hora_inicio) * 60;
        if hora_min == 0:
            hora_min = 23 * 60;
        minutos = minuto_inicio - minuto_termino;
        duracao = hora_min + minutos;
        print("A duração do jogo foi de %i minutos"%duracao);
    elif hora_inicio > hora_termino and minuto_inicio < minuto_termino:
        hora_min = (hora_termino + 24 - hora_inicio) * 60;
        minutos = minuto_termino - minuto_inicio;
        duracao = hora_min + minutos; 
        print("A duração do jogo foi de %i minutos"%duracao);
    elif hora_inicio > hora_termino and minuto_inicio >= minuto_termino:
        hora_min = (hora_termino + 24 - hora_inicio) * 60;
        minutos = minuto_inicio - minuto_termino;
        duracao = hora_min + minutos;
        print("A duração do jogo foi de %i minutos"%duracao);
        
def main():
    duracao_jogo();
    
main();