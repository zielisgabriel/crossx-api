from server import app;
from flask import jsonify, request;
from models.Student import Student;

@app.get("/students/find")
def findByStudentName():
    name = request.args.get("name")

    if name is None:
        students = Student.query.all();

        return jsonify({"students": students});

    students = Student.query.filter(Student.name.ilike(f"{name}%")).all();

    return jsonify({"students": students});