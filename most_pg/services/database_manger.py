from ..settings import DatabaseSettings
from alembic import command, config
import asyncio
import most_pg
from importlib import resources

class DatabaseManager:
    def __init__(self, settings: DatabaseSettings):
        self._settings = settings
    
    def run_migrations(self):
        alembic_ini_path = resources.files(most_pg) / 'alembic.ini'
        alembic_cfg = config.Config(alembic_ini_path)
        alembic_cfg.set_main_option("sqlalchemy.url", self._settings.url)
        command.upgrade(config=alembic_cfg, revision="head")
    
    async def init_database(self):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.run_migrations)