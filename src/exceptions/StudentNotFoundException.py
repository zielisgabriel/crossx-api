class StudentNotFoundException(Exception):
    def __init__(self):
        super().__init__("Aluno não encontrado.")