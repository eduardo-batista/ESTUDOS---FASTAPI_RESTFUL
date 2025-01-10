from typing import Generic, Type, TypeVar

from api.src.repository.base import BaseRepository

T = TypeVar('T', bound=BaseRepository)

class BaseService(Generic[T]):
    def __init__(self, repository: Type[T]):
        self.repository = repository()
    
    async def get(self, id: int): 
        return await self.repository.get(id)
    
    async def get_all(self): 
        return await self.repository.get_all()
    
    async def create(self, obj_in): 
        return await self.repository.create(obj_in)
    
    async def update(self, obj_in, id): 
        return await self.repository.update(obj_in, id)
    
    async def delete(self, id: int): 
        return await self.repository.delete(id)