from typing import List
from fastapi import APIRouter, status

from api.src.model.schema.example_request import ExampleRequest
from api.src.service.example_service import ExampleService

example_router = APIRouter(prefix='/example')
service = ExampleService()

# GET /example/{id}
@example_router.get(
        '/{id}', status_code=status.HTTP_200_OK,
        description="Retrieves an 'Example' object based on the provided ID."
        )
async def get(id: int) -> ExampleRequest:
    return await service.get(id)

# GET /example
@example_router.get(
        '/', status_code=status.HTTP_200_OK,
        description="Retrieves all 'Example' objects."
        )
async def get_all() -> List[ExampleRequest]:
    return await service.get_all()

# POST /example
@example_router.post(
        '/', status_code=status.HTTP_201_CREATED,
        description="Creates a new 'Example' object with the provided data."
        )
async def create(example_request: ExampleRequest) -> ExampleRequest:
    return await service.create(example_request.__get_entity__())

# PUT /example/{id}
@example_router.put(
        '/{id}', status_code=status.HTTP_200_OK,
        description="Updates an existing 'Example' object with the provided data."
        )
async def update(example_request: ExampleRequest, id: int) -> ExampleRequest:
    return await service.update(example_request.__get_entity__(), id)

# DELETE /example/{id}
@example_router.delete(
        '/{id}', status_code=status.HTTP_204_NO_CONTENT,
        description="Deletes an 'Example' object based on the provided ID."
        )
async def delete(id: int) -> None:
    return await service.delete(id)
