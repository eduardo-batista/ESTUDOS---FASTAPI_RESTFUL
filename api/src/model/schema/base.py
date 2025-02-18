from typing import Optional
from pydantic import BaseModel


class BaseSchema(BaseModel):
    id: Optional[int] = None

    def __get_entity__(self):
        raise NotImplementedError(f"{self.__class__.__name__} must implement '__get_entity__' method")

    class Config:
        from_attributes = True