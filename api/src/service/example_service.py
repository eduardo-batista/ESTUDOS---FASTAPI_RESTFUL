from api.src.model.entity.example_entity import Example
from api.src.model.schema.example_schema import ExampleSchema
from api.src.repository.example_repository import ExampleRepository
from .base import BaseService

class ExampleService(BaseService[ExampleRepository, Example, ExampleSchema]):
    def __init__(self):
        super().__init__(ExampleRepository, Example, ExampleSchema)
        