from typing import Generic, Sequence, Type, TypeVar

from api.src.model.entity.base import BaseEntity
from api.src.model.schema.base import BaseSchema
from api.src.repository.base import BaseRepository

R = TypeVar('R', bound=BaseRepository)
T = TypeVar('T', bound=BaseEntity)
S = TypeVar('S', bound=BaseSchema)

class BaseService(Generic[R, T, S]):
    def __init__(self, repository: Type[R], entity: Type[T], schema: Type[S]):
        self.repository = repository(entity)
        self.schema = schema
    
    async def get(self, id: int) -> S | None:
        """
        Retrieves an object based on the provided ID.
        
        Args:
        - id (int): The ID of the object to retrieve.

        Returns:
        - The object with the provided ID.
        """
        entity = await self.repository.get(id)
        if entity is None:
            return None
        return self.schema.model_validate(entity)
    
    async def get_all(self) -> Sequence[S]:
        """
        Retrieves all objects.
        
        Returns:
        - List of objects.
        """
        entities = await self.repository.get_all()
        return [self.schema.model_validate(entity) for entity in entities]
    
    async def create(self, obj_in: T) -> S:
        """
        Creates a new object with the provided data.

        Args:
        - obj_in: Data to create the new object.
        
        Returns:
        - The newly created object.
        """
        entity = await self.repository.create(obj_in)
        return self.schema.model_validate(entity)
    
    async def update(self, obj_in: T, id: int) -> S:
        """
        Updates an existing object with the provided data.

        Args:
        - obj_in: Data to update the object.
        - id (int): The ID of the object to update.
        
        Returns:
        - The updated object.
        """
        entity = await self.repository.update(obj_in, id)
        return self.schema.model_validate(entity)
    
    async def delete(self, id: int) -> None:
        """
        Deletes an object based on the provided ID.

        Args:
        - id (int): The ID of the object to delete.

        Returns:
        - No content.
        """
        return await self.repository.delete(id)