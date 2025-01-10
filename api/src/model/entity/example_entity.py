from sqlalchemy import Column, Integer
from .base import BaseEntity

class Example(BaseEntity):
    __tablename__ = 'entity_example'

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return (f"<EntityExample(id={self.id})>")
    

    def to_dict(self):
        return {
            "id": self.id,
        }