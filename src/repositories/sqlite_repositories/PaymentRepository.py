from typing import List
from models.Payment import Payment
from repositories.PaymentRepositoryInterface import PaymentRepositoryInterface


class PaymentRepository(PaymentRepositoryInterface):
    def find_by_student_id(self, student_id: int) -> List[Payment]:
        payments = Payment.query.filter_by(student_id=student_id).all()

        return payments