from .base import BaseRepository
from api.src.model.entity.example_entity import Example
from api.database.database import DatabaseConfig


class ExampleRepository(BaseRepository[Example]):
    
    def __init__(self):
        session_local = DatabaseConfig().get_async_session_local()
        self.session = session_local()
        super().__init__(Example, self.session)
