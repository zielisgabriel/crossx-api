from repositories.PaymentRepositoryInterface import PaymentRepositoryInterface
from repositories.StudentRepositoryInterface import StudentRepositoryInterface
from server import db
from models.Payment import Payment
from datetime import datetime
from dateutil.relativedelta import relativedelta
from decimal import Decimal
from exceptions.StudentNotFoundException import StudentNotFoundException
from flask import request

from typing import Any

class MakePaymentService:
    def __init__(self, studentRepository: StudentRepositoryInterface, paymentRepository: PaymentRepositoryInterface):
        self.studentRepositoryInterface = studentRepository
        self.paymentRepositoryInterface = paymentRepository

    def execute(self, student_id, data: Any):
        student = self.studentRepositoryInterface.find_by_id(student_id=student_id)

        if student is None:
            raise StudentNotFoundException()

        if student.status == "Matriculado":
            raise Exception("O aluno já esta matriculado.")
    
        payment = Payment(
            student_id=student_id,
            amount=Decimal(data["amount"]),
            payment_method=data["payment_method"],
            payment_date=datetime.now()
        )
    
        student.status = "Matriculado"
        student.registration_date = datetime.now()
        student.due_date = datetime.now() + relativedelta(months=1)
    
        db.session.add(payment)
        db.session.commit()