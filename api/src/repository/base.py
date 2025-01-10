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
        async with self.db.begin():
            result = await self.db.execute(query)
            response = result.scalars().first()
            await self.db.close()
            return response

    async def get_all(self) -> List[T]:
        query = select(self.entity)
        async with self.db.begin():
            result = await self.db.execute(query)
            response = result.scalars().all()
            await self.db.close()
            return response

    async def create(self, obj_in: T) -> T:
        async with self.db.begin():
            self.db.add(obj_in)
            await self.db.flush()
            await self.db.commit()
            await self.db.close()
            return obj_in

    async def update(self, obj_in: T) -> T:
        async with self.db.begin():
            await self.db.merge(obj_in)
            await self.db.commit()
            await self.db.close()
            return obj_in

    async def delete(self, id: int) -> None:
        async with self.db.begin():
            query = select(self.entity).filter(getattr(self.entity, self.primary_key_name) == id)
            result = await self.db.execute(query)
            obj = result.scalars().first()
            if obj:
                await self.db.delete(obj)
                await self.db.commit()
            await self.db.close()