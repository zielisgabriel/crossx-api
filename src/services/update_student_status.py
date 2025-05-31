from datetime import datetime
from models.Student import Student;
from server import app, db;

def update_student_status():
    with app.app_context():
        students = Student.query.filter(
            Student.status == "Matriculado",
            Student.due_date < datetime.now()
        ).all();

        for student in students:
            student.status = "Pendente";

        db.session.commit();