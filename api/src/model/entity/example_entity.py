from sqlalchemy import Column, Integer, String
from .base import BaseEntity

class Example(BaseEntity):
    __tablename__ = 'entity_example'

    id = Column(Integer, primary_key=True)
    example_field = Column(String(45), primary_key=True)

    def __repr__(self):
        return (f"<EntityExample(id={self.id}, (example_field={self.example_field})>")
    

    def to_dict(self):
        return {
            "id": self.id,
            "example_field": self.example_field
        }