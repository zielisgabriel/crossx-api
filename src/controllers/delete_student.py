from server import app, db;
from flask import jsonify;
from models.Student import Student;

from exceptions.StudentNotFoundException import StudentNotFoundException;

@app.delete("/students/delete/<int:student_id>")
def deleteStudent(student_id):
    try:
        student = db.session.query(Student).filter_by(student_id=student_id).first();

        if student is None:
            raise StudentNotFoundException();

        db.session.delete(student);
        db.session.commit();    

        return jsonify({"message": "Student deleted"});
    except Exception as e:
        return jsonify({"message": str(e)}), 400;