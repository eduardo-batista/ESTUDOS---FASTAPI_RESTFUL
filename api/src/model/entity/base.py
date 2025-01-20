from sqlalchemy.orm import DeclarativeBase

class BaseEntity(DeclarativeBase):
    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: The dictionary representation of the instance.
        """
        # Obtém todos os atributos do objeto, incluindo os campos da tabela
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}