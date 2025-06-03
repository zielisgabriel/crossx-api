from server import app, db;
from models.Student import Student;
from flask import jsonify, request, Response;
from datetime import datetime;

@app.put("/students/update/<int:student_id>")
def update_student(student_id):
    student = Student.query.filter_by(student_id=student_id).first();

    if student is None:
        return jsonify({"message": "Student not found"}), 404;

    data = request.get_json();

    if (data["status"] == "Não Matriculado"):
        student.registration_date = None;
        student.termination_date = datetime.now();
        student.due_date = None;

    student.name = data["name"];
    student.city = data["city"];
    student.state = data["state"];
    student.phone = data["phone"];
    student.address = data["address"];
    student.status = data["status"];

    db.session.commit();

    return Response(status=200);