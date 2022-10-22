class TipoAluno:
    matricula = 0
    nome = ""
    p1 = 0.0
    p2 = 0.0
    media = 0.0
    
def main():
    aluno = TipoAluno()
    aluno.matricula = int(input("Digite a matricula: "))
    aluno.nome = input("Digite o nome: ")
    aluno.p1 = float(input("Digite a P1: "))
    aluno.p2 = float(input("Digite a P2: "))
    aluno.media = (aluno.p1 + aluno.p2)/2
    
main()