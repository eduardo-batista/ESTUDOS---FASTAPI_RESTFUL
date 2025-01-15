import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConfig:
    def __init__(self):
        load_dotenv()
        self.DB_NAME = os.getenv('DB_NAME', 'example_db')
        self.DB_USER = os.getenv('DB_USER', 'example_user')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'example_password')
        self.DB_HOST = os.getenv('DB_HOST', 'db_service')
        self.DB_PORT = os.getenv('DB_PORT', '5432')
        self.DB_TYPE = os.getenv('DB_TYPE', 'postgresql')
        self.DB_ASYNC = os.getenv('DB_ASYNC', 'asyncpg')

    def get_database_url(self):
        if self.DB_PORT:
            return f"{self.DB_TYPE}+{self.DB_ASYNC}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        else:
            return f"{self.DB_TYPE}+{self.DB_ASYNC}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}"

    def get_async_engine(self):
        return create_async_engine(self.get_database_url(), echo=True)

    def get_async_session_local(self):
        engine = self.get_async_engine()
        return sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)