from contextlib import asynccontextmanager
from fastapi import HTTPException
from sqlalchemy import select
from typing import Type, TypeVar, Generic, List
from api.database.database import DatabaseConfig
from api.src.model.entity.base import BaseEntity

T = TypeVar('T', bound=BaseEntity)

class BaseRepository(Generic[T]):
    def __init__(self, entity: Type[T]):
        self.entity = entity
        self.session_factory = DatabaseConfig().get_async_session_local()
        self.primary_key_name = self._get_primary_key_name()

    def _get_primary_key_name(self):
        """
        Retrieves the name of the primary key of the entity.

        This method uses SQLAlchemy's ORM to inspect the entity and 
        retrieve the name of its primary key.

        Returns:
            str: The name of the primary key for the entity.

        Example:
            primary_key_name = self._get_primary_key_name()
        """
        mapper = self.entity.__mapper__
        primary_key = mapper.primary_key[0]
        return primary_key.name

    async def get(self, id: int) -> T:
        """
        Retrieves an object based on the provided ID.
        
        Args:
        - id (int): The ID of the object to retrieve.

        Returns:
        - The object with the provided ID.
        """
        query = select(self.entity).filter(getattr(self.entity, self.primary_key_name) == id)
        async with self.get_session() as session:
            result = await session.execute(query)
            return result.scalars().first()

    async def get_all(self) -> List[T]:
        """
        Retrieves all objects.
        
        Returns:
        - List of objects.
        """
        query = select(self.entity)
        async with self.get_session() as session:
            result = await session.execute(query)
            return result.scalars().all()

    async def create(self, obj_in: T) -> T:
        """
        Creates a new object with the provided data.

        Args:
        - obj_in: Data to create the new object.
        
        Returns:
        - The newly created object.
        """
        async with self.get_session() as session:
            session.add(obj_in)
            await session.commit()
            return obj_in

    async def update(self, obj_in: T, id: int) -> T:
        """
        Updates an existing object with the provided data.

        Args:
        - obj_in: Data to update the object.
        - id (int): The ID of the object to update.
        
        Returns:
        - The updated object.
        """
        async with self.get_session() as session:
            query = select(self.entity).filter(getattr(self.entity, self.primary_key_name) == id)
            result = await session.execute(query)
            obj = result.scalars().first()
            
            if not obj:
                raise HTTPException(404, f'Não foi encontrado um registro com ID: {id}.')
            
            for key, value in obj_in.to_dict().items():
                if key != 'id':
                    setattr(obj, key, value)
            await session.commit()
            return obj

    async def delete(self, id: int) -> None:
        """
        Deletes an object based on the provided ID.

        Args:
        - id (int): The ID of the object to delete.

        Returns:
        - No content.
        """
        async with self.get_session() as session:
            query = select(self.entity).filter(getattr(self.entity, self.primary_key_name) == id)
            result = await session.execute(query)
            obj = result.scalars().first()
            
            if not obj:
                raise HTTPException(404, f'Não foi encontrado um registro com ID: {id}.')
            
            if obj:
                await session.delete(obj)
                await session.commit()
                
    @asynccontextmanager
    async def get_session(self):
        """
        Provides an asynchronous context manager for a database session.

        This method creates and yields a session object, ensuring that the session 
        is properly closed after usage, even if an exception occurs.

        Yields:
            AsyncSession: The session object used for database operations.

        Example:
            async with self.get_session() as session:
                # Perform database operations
        """
        session = self.session_factory()
        try:
            yield session
        finally:
            await session.close()