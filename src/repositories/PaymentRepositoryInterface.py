from abc import ABC, abstractmethod
from typing import List
from models.Payment import Payment

class PaymentRepositoryInterface:
    @abstractmethod
    def find_by_student_id(self, student_id: int) -> List[Payment]:
        pass