from api.src.repository.example_repository import ExampleRepository
from .base import BaseService

class ExampleService(BaseService[ExampleRepository]):
    def __init__(self):
        super().__init__(ExampleRepository)
        