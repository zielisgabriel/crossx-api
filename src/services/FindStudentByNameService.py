from repositories.StudentRepositoryInterface import StudentRepositoryInterface

class FindStudentByNameService:
    def __init__(self, respository: StudentRepositoryInterface):
        self.studentRepositoryInterface = respository

    def execute(self, student_name):
        students = self.studentRepositoryInterface.find_by_name(student_name=student_name)

        return students