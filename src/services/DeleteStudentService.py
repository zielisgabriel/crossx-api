from exceptions.StudentNotFoundException import StudentNotFoundException
from repositories.StudentRepositoryInterface import StudentRepositoryInterface
from server import db

class DeleteStudentService:
    def __init__(self, repository: StudentRepositoryInterface):
        self.studentRepositoryInterface = repository

    def execute(self, student_id):
        student = self.studentRepositoryInterface.find_by_id(student_id=student_id)

        if student is None:
            raise StudentNotFoundException()
    
        if student.registration_date != None and student.status == "Matriculado":
            raise Exception("O aluno não pode ser removido, pois está matriculado.")

        db.session.delete(student)
        db.session.commit()