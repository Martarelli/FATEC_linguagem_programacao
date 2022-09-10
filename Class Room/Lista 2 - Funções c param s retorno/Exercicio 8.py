# 8. (Função sem retorno com parâmetro) Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno. Aqui deverá ocorrer nas duas funções, PASSAGEM DE PARÂMETRO POR VALOR.
def media(p1, p2):
    x = (p1 + p2)/2;
    aprovado(x);
    
def aprovado(media):
    if media >= 6:
        print("APROVADOOOOOO");
    else:
        print("REPROVADOOOO :C");
        
def main():
    p1 = int(input("Digite a nota p1: "));
    p2 = int(input("Digite a nota p2: "));
    media(p1, p2);


main();