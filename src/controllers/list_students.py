from server import app;
from flask import jsonify;
from models.Student import Student;

@app.get("/students/list")
def listStudents():
    students = Student.query.all();

    return jsonify({"students": students});