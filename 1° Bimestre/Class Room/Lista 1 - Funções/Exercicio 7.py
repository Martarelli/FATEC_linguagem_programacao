# 7. (Função sem retorno sem parâmetro) Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a A, deverá calcular a média aritimética das notas dos alunos, se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final.
def media():
    print("Olá, tudo bem?");
    nota1 = float(input("Digite a primeira nota: "));
    nota2 = float(input("Digite a segunda nota: "));
    nota3 = float(input("Digite a terceira nota: "));
    tipo_media = input("Digite o tipo de media - Aritimética(A) Ponderada(P): ").upper();4

    if tipo_media == "A":
        media = (nota1 + nota2 + nota3) / 3 ;
        print("A média do aluno foi de %.2f"%media);
    elif tipo_media == "P":
        media = (nota1 * 5 + nota2 * 3 + nota3 * 2)/(5 + 3 + 2);
        print("A média do aluno foi de %.2f"%media);
    else:
        print("Opção inválida");

def main():
    media();

main();