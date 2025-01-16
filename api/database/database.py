import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConfig:
    _engine = None
    def __init__(self):
        load_dotenv()
        self.DB_NAME = os.getenv('DB_NAME') or 'example_db'
        self.DB_USER = os.getenv('DB_USER') or 'example_user'
        self.DB_PASSWORD = os.getenv('DB_PASSWORD') or 'example_password'
        self.DB_HOST = os.getenv('DB_HOST') or 'db_service'
        self.DB_PORT = os.getenv('DB_PORT') or '5432'
        self.DB_TYPE = os.getenv('DB_TYPE') or 'postgresql'
        self.DB_ASYNC = os.getenv('DB_ASYNC') or 'asyncpg'

    def get_database_url(self) -> str:
        if self.DB_PORT:
            return f"{self.DB_TYPE}+{self.DB_ASYNC}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"{self.DB_TYPE}+{self.DB_ASYNC}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}"

    def get_async_engine(self) -> AsyncEngine:
        if not self._engine:
            self._engine = create_async_engine(
                self.get_database_url(),
                echo=False,
                pool_pre_ping=True,
                pool_size=10,
                max_overflow=10,
                pool_timeout=30
            )
        return self._engine

    def get_async_session_local(self) -> AsyncSession:
        engine = self.get_async_engine()
        return sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)