class Pessoa:
    def __init__(self,cpf,nome):
        self.nome = nome
        self.cpf = cpf
class Aluno(Pessoa):
    def __init__(self,nome,prontuario,cpf,curso):
        Pessoa.__init__(self,nome,cpf)
        self.curso=curso
        self.prontuario=prontuario
    def getCurso(self):
        return self.curso
