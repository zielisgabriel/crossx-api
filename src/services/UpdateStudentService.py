from flask import request
from repositories.StudentRepositoryInterface import StudentRepositoryInterface
from exceptions.StudentNotFoundException import StudentNotFoundException
from server import db
from datetime import datetime

from typing import Any

class UpdateStudentService:
    def __init__(self, repository: StudentRepositoryInterface):
        self.studentRepositoryInterface = repository

    def execute(self, student_id, data: Any):
        student = self.studentRepositoryInterface.find_by_id(student_id=student_id)

        if student is None:
            raise StudentNotFoundException()
        
        if data["status"] == "Não Matriculado" and student.status == "Matriculado":
            raise Exception("O status nao pode ser atualizado, pois esta matriculado.")

        if data["status"] == "Matriculado" and student.registration_date == None and student.status == "Não Matriculado":
            raise Exception("O aluno nao pode ser matriculado, pois não existe pagamento válido.")
        
        if data["status"] == "Não Matriculado" and student.status == "Pendente":
            student.registration_date = None
            student.termination_date = datetime.now()
            student.due_date = None

        student.name = data["name"]
        student.city = data["city"]
        student.state = data["state"]
        student.phone = data["phone"]
        student.address = data["address"]
        student.status = data["status"]

        db.session.commit()