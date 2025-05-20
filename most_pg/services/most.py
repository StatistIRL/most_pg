import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from ..engine import get_async_session_factory
from alembic.config import Config
from alembic import command
from sqlalchemy.dialects.postgresql import insert
from ..models.calls import Call
from .. import _types as json_types

from ..settings import DatabaseSettings

class MostPGDatabaseService:
    def __init__(self, settings: DatabaseSettings):
        self._settings = settings
    
    def run_migrations(self, ):
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option("sqlalchemy.url", self._settings.url)
        command.upgrade(config=alembic_cfg, revision="head")
    
    async def init_database(self):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.run_migrations)
    
    async def __aenter__(self):
        async_session_factory = get_async_session_factory(self._settings.url)
        self.__session = async_session_factory()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.__session:
            if exc_type is None:
                await self.__session.commit()
            else:
                await self.__session.rollback()
            await self.__session.close()
            
    async def add_call(self, call: json_types.Call, flush: bool = False):
        call = Call(**call.to_dict())
        
        self.__session.add(call)
        
        if flush:
            await self.__session.flush()
        
        return call
        