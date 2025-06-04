from repositories.StudentRepositoryInterface import StudentRepositoryInterface


class ListStudentsService:
    def __init__ (self, repository: StudentRepositoryInterface):
        self.studentRepositoryInterface = repository

    def execute(self):
        students = self.studentRepositoryInterface.list_all()

        return students