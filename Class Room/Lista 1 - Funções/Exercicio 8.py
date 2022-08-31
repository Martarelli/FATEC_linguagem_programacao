# 8. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.

def duracao_jogo():
    
    hora_inicio = int(input("Informe a hora de inicio do jogo: "))
    minuto_inicio = int(input("Informe os minutos de inicio do jogo: "))
    hora_termino = int(input("Informe a hora de termino do jogo: "))
    minuto_termino = int(input("Informe os minutos do termino do jogo: "))

    