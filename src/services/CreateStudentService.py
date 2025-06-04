from models.Student import Student
from typing import Any
from server import db

class CreateStudentService:
    def execute(self, data: Any):
        name = data["name"]
        city = data["city"]
        state = data["state"]
        phone = data["phone"]
        address = data["address"]
        registration_date = None
        termination_date = None
        due_date = None

        student = Student(
            name=name,
            city=city,
            state=state,
            phone=phone,
            address=address,
            registration_date=registration_date,
            termination_date=termination_date,
            due_date=due_date,
        )

        db.session.add(student)
        db.session.commit()