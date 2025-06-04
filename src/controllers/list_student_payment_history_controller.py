from repositories.sqlite_repositories.PaymentRepository import PaymentRepository
from repositories.sqlite_repositories.StudentRepository import StudentRepository
from server import app
from flask import jsonify
from services.ListStudentPaymentHistoryService import ListStudentPaymentHistoryService

@app.get("/payments/list/<int:student_id>")
def list_student_payment_history(student_id):
    try:
        paymentRepository = PaymentRepository()
        studentRepository = StudentRepository()
        listStudentPaymentHistoryService = ListStudentPaymentHistoryService(studentRepository, paymentRepository)
        payments = listStudentPaymentHistoryService.execute(student_id=student_id)

        return jsonify({"payments": payments})
    except Exception as e:
        return jsonify({"message": str(e)}), 400