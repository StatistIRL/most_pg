from ..engine import get_async_session_factory
from ..settings import DatabaseSettings
from sqlalchemy.ext.asyncio import AsyncSession

class BaseRepository:
    def __init__(self, settings: DatabaseSettings):
        self._settings = settings
    
    async def __aenter__(self):
        async_session_factory = get_async_session_factory(self._settings.url)
        self._session: AsyncSession = async_session_factory()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            if exc_type is None:
                await self._session.commit()
            else:
                await self._session.rollback()
            await self._session.close()