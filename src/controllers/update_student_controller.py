from server import app
from flask import jsonify, request, Response
from services.UpdateStudentService import UpdateStudentService
from repositories.sqlite_repositories.StudentRepository import StudentRepository

@app.put("/students/update/<int:student_id>")
def update_student(student_id):
    try:
        data = request.get_json()

        studentRepository = StudentRepository()
        updateStudentService = UpdateStudentService(studentRepository)
        updateStudentService.execute(student_id=student_id, data=data)

        return Response(status=200)
    except Exception as e:
        return jsonify({"message": str(e)}), 400