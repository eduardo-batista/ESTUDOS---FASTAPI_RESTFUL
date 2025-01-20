from api.src.model.entity.example_entity import Example
from api.src.repository.example_repository import ExampleRepository
from .base import BaseService

class ExampleService(BaseService[ExampleRepository, Example]):
    def __init__(self):
        super().__init__(ExampleRepository)
        