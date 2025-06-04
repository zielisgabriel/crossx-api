from repositories.sqlite_repositories.StudentRepository import StudentRepository
from server import app
from flask import jsonify
from services.ListStudentsService import ListStudentsService

@app.get("/students/list")
def listStudents():
    try:
        studentRepository = StudentRepository()
        listStudentsService = ListStudentsService(studentRepository)
        students = listStudentsService.execute()

        return jsonify({"students": students})
    except Exception as e:
        return jsonify({"message": str(e)}), 400