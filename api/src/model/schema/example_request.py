from pydantic import BaseModel, Field

from api.src.model.entity.example_entity import Example

class ExampleRequest(BaseModel):
    example_field: str = Field(...,
        title='Campo de Exemplo',
        description='Campo de Exemplo para fins didáticos'
    )

    def __get_entity__(self):
        return Example(
            self.example_field
        )