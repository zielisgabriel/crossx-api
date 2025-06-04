from repositories.sqlite_repositories.StudentRepository import StudentRepository
from server import app
from flask import jsonify, request, Response
from exceptions.StudentNotFoundException import StudentNotFoundException
from services.MakePaymentService import MakePaymentService

from repositories.sqlite_repositories.PaymentRepository import PaymentRepository

@app.post("/payments/make/<int:student_id>")
def make_payment(student_id):
    try:
        data = request.get_json()

        studentRepository = StudentRepository()
        paymentRepository = PaymentRepository()
        makePaymentService = MakePaymentService(studentRepository, paymentRepository)
        makePaymentService.execute(student_id=student_id, data=data)
        
        return Response(status=201)
    except (Exception) as e:
        if isinstance(e, StudentNotFoundException):
            return jsonify({"message": str(e)}), 404
        elif isinstance(e, Exception):
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "Unhandled error"}), 500
    