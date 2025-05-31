class StudentNotFoundException(Exception):
    def __init__(self):
        super().__init__("Student not found");