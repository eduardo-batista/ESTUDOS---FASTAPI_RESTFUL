from typing import Generic, List, Type, TypeVar

from api.src.repository.base import BaseRepository

T = TypeVar('T', bound=BaseRepository)

class BaseService(Generic[T]):
    def __init__(self, repository: Type[T]):
        self.repository = repository()
    
    async def get(self, id: int) -> T:
        """
        Retrieves an object based on the provided ID.
        
        Args:
        - id (int): The ID of the object to retrieve.

        Returns:
        - The object with the provided ID.
        """
        return await self.repository.get(id)
    
    async def get_all(self) -> List[T]:
        """
        Retrieves all objects.
        
        Returns:
        - List of objects.
        """
        return await self.repository.get_all()
    
    async def create(self, obj_in) -> T:
        """
        Creates a new object with the provided data.

        Args:
        - obj_in: Data to create the new object.
        
        Returns:
        - The newly created object.
        """
        return await self.repository.create(obj_in)
    
    async def update(self, obj_in, id) -> T:
        """
        Updates an existing object with the provided data.

        Args:
        - obj_in: Data to update the object.
        - id (int): The ID of the object to update.
        
        Returns:
        - The updated object.
        """
        return await self.repository.update(obj_in, id)
    
    async def delete(self, id: int) -> None:
        """
        Deletes an object based on the provided ID.

        Args:
        - id (int): The ID of the object to delete.

        Returns:
        - No content.
        """
        return await self.repository.delete(id)