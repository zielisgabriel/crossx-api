from server import app
from flask import request, jsonify, Response

from services.CreateStudentService import CreateStudentService

@app.post("/students/create")
def createStudent():
    try:
        data = request.get_json()

        createStudentService = CreateStudentService()
        createStudentService.execute(data)

        return Response(status=201)
    except Exception as e:
        return jsonify({"message": str(e)}), 400