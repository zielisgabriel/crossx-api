from server import app, db;
from flask import jsonify, Response;
from models.Student import Student;

from exceptions.StudentNotFoundException import StudentNotFoundException;

@app.delete("/students/delete/<int:student_id>")
def deleteStudent(student_id):
    try:
        student = db.session.query(Student).filter_by(student_id=student_id).first();

        if student is None:
            raise StudentNotFoundException();
    
        if student.status == "Matriculado":
            raise Exception("O aluno não pode ser removido, pois está matriculado.");

        db.session.delete(student);
        db.session.commit();

        return Response(status=200);
    except Exception as e:
        return jsonify({"message": str(e)}), 400;