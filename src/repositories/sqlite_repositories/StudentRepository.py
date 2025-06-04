from typing import List
from repositories.StudentRepositoryInterface import StudentRepositoryInterface
from models.Student import Student
from server import db

class StudentRepository(StudentRepositoryInterface):
    def find_by_name(self, student_name: str | None):
        if student_name is None:
            students = Student.query.all()
            return students

        students = Student.query.filter(Student.name.ilike(f"{student_name}%")).all()
        return students

    def find_by_id(self, student_id: int) -> Student | None:
        student = Student.query.filter_by(student_id=student_id).first()

        return student

    def list_all(self) -> List[Student]:
        students = Student.query.all()

        return students