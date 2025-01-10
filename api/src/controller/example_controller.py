from fastapi import APIRouter, status

from api.src.service.example_service import ExampleService
from api.src.model.entity.example_entity import Example

example_router = APIRouter(prefix='/example')
service = ExampleService()

@example_router.get('/{id}', status_code=status.HTTP_200_OK)
async def get(id: int):
    return await service.get(id)

@example_router.get('/', status_code=status.HTTP_200_OK)
async def get_all():
    return await service.get_all()

@example_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(example_request: Example):
    return await service.create(example_request)

@example_router.put('/{id}', status_code=status.HTTP_200_OK)
async def update(example_request: Example, id: int):
    return await service.update(example_request, id)

@example_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def get_all(id: int):
    return await service.get_all(id)