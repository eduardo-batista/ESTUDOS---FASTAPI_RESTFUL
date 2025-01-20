from fastapi import APIRouter, status

from api.src.model.schema.example_request import ExampleRequest
from api.src.service.example_service import ExampleService

example_router = APIRouter(prefix='/example')
service = ExampleService()

@example_router.get('/{id}', status_code=status.HTTP_200_OK)
async def get(id: int):
    return await service.get(id)

@example_router.get('/', status_code=status.HTTP_200_OK)
async def get_all():
    return await service.get_all()

@example_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(example_request: ExampleRequest):
    return await service.create(example_request.__get_entity__())

@example_router.put('/{id}', status_code=status.HTTP_200_OK)
async def update(example_request: ExampleRequest, id: int):
    return await service.update(example_request.__get_entity__(), id)

@example_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int):
    return await service.delete(id)