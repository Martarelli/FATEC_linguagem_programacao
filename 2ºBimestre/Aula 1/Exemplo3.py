class TipoEndereco:
    logradouro: ""
    numero = 0 
    bairro = ""
    cep = 0

class TipoAluno:
    matricula = 0
    nome = ""
    endereco = TipoEndereco()
    p1 = 0.0
    p2 = 0.0
    media = 0.0

def main():
    aluno = TipoAluno()
    aluno.matricula = int(input("Digite a matricula: "))
    aluno.endereco.logradouro = input("Digite o logradouro: ")
    