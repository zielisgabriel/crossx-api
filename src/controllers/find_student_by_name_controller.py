from repositories.sqlite_repositories.StudentRepository import StudentRepository
from services.FindStudentByNameService import FindStudentByNameService
from server import app
from flask import jsonify, request

@app.get("/students/find")
def findByStudentName():
    try:
        student_name = request.args.get("name")

        studentRepository = StudentRepository()
        findStudentByNameService = FindStudentByNameService(studentRepository)
        students = findStudentByNameService.execute(student_name=student_name)

        return jsonify({"students": students})
    except Exception as e:
        return jsonify({"message": str(e)}), 400