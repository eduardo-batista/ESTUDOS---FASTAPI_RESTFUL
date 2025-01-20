from .base import BaseRepository
from api.src.model.entity.example_entity import Example


class ExampleRepository(BaseRepository[Example]):
    
    def __init__(self):
        super().__init__(Example)
