from exceptions.StudentNotFoundException import StudentNotFoundException
from repositories.StudentRepositoryInterface import StudentRepositoryInterface
from repositories.PaymentRepositoryInterface import PaymentRepositoryInterface

class ListStudentPaymentHistoryService:
    def __init__(self, studentRespository: StudentRepositoryInterface, paymentRepository: PaymentRepositoryInterface):
        self.studentRepositoryInterface = studentRespository
        self.paymentRepositoryInterface = paymentRepository

    def execute(self, student_id):
        student = self.studentRepositoryInterface.find_by_id(student_id=student_id)

        if student is None:
            raise StudentNotFoundException()
        
        payments = self.paymentRepositoryInterface.find_by_student_id(student_id=student_id)

        return payments