from repositories.sqlite_repositories.StudentRepository import StudentRepository
from server import app
from flask import jsonify, Response
from services.DeleteStudentService import DeleteStudentService

@app.delete("/students/delete/<int:student_id>")
def deleteStudent(student_id):
    try:
        studentRepository = StudentRepository()
        deleteStudentService = DeleteStudentService(studentRepository)
        deleteStudentService.execute(student_id)

        return Response(status=200)
    except Exception as e:
        return jsonify({"message": str(e)}), 400