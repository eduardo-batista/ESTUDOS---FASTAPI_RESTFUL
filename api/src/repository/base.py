from contextlib import asynccontextmanager
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, TypeVar, Generic, List
from api.src.model.entity.base import BaseEntity

T = TypeVar('T', bound=BaseEntity)

class BaseRepository(Generic[T]):
    def __init__(self, entity: Type[T], db: AsyncSession):
        self.entity = entity
        self.db = db
        self.primary_key_name = self._get_primary_key_name()

    def _get_primary_key_name(self):
        mapper = self.entity.__mapper__
        primary_key = mapper.primary_key[0]
        return primary_key.name

    async def get(self, id: int) -> T:
        query = select(self.entity).filter(getattr(self.entity, self.primary_key_name) == id)
        async with self.get_session() as session:
            result = await session.execute(query)
            return result.scalars().first()

    async def get_all(self) -> List[T]:
        query = select(self.entity)
        async with self.get_session() as session:
            result = await session.execute(query)
            return result.scalars().all()

    async def create(self, obj_in: T) -> T:
        async with self.get_session() as session:
            session.add(obj_in)
            await session.flush()
            await session.commit()
            return obj_in

    async def update(self, obj_in: T) -> T:
        async with self.get_session() as session:
            await session.merge(obj_in)
            await session.commit()
            return obj_in

    async def delete(self, id: int) -> None:
        async with self.get_session() as session:
            query = select(self.entity).filter(getattr(self.entity, self.primary_key_name) == id)
            result = await session.execute(query)
            obj = result.scalars().first()
            if obj:
                await session.delete(obj)
                await session.commit()
                
    @asynccontextmanager
    async def get_session(self):
        session = self.session_factory()
        try:
            yield session
        finally:
            await session.close()