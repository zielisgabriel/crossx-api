from abc import ABC, abstractmethod
from typing import List
from models.Student import Student

class StudentRepositoryInterface(ABC):
    @abstractmethod
    def find_by_name(self, student_name: str | None) -> List[Student]:
        pass

    @abstractmethod
    def find_by_id(self, student_id: int) -> Student | None:
        pass

    @abstractmethod
    def list_all(self) -> List[Student]:
        pass