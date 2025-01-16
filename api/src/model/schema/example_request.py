
from pydantic import BaseModel, Field

class ExampleRequest(BaseModel):
    example_field: str = Field(...,
        title='Campo de Exemplo',
        description='Campo de Exemplo para fins didáticos'
    )