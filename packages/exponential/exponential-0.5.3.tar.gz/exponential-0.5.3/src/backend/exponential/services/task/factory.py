from exponential.services.task.manager import TaskService
from exponential.services.factory import ServiceFactory


class TaskServiceFactory(ServiceFactory):
    def __init__(self):
        super().__init__(TaskService)

    def create(self):
        # Here you would have logic to create and configure a TaskService
        return TaskService()
