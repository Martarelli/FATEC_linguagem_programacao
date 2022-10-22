class TipoAluno:
    matricula = 0
    nome = ""
    p1 = 0.0
    p2 = 0.0
    media = 0.0
    
def main():
    vet_aluno = []
    for i in range(2): 
        aluno = TipoAluno()
        aluno.matricula = int(input("Digite a matricula: "))
        aluno.nome = input("Digite o nome: ").upper()
        aluno.p1 = float(input("Digite a P1: "))
        aluno.p2 = float(input("Digite a P2: "))
        aluno.media = (aluno.p1 + aluno.p2)/2
        vet_aluno.append(aluno)
    for i in range(len(vet_aluno)):
        print("\nMatricula: ", vet_aluno[i].matricula, " Nome: ", vet_aluno[i].nome, " P1: ", vet_aluno[i].p1, " P2: ", vet_aluno[i].p2, " Média: ", vet_aluno[i].media)
    
main()