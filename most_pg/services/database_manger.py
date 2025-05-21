import os
from ..settings import DatabaseSettings
from alembic import command, config
import asyncio

script_dir = os.path.dirname(os.path.realpath(__file__))

ALEMBIC_INI_PATH = os.path.abspath(os.path.join(script_dir, "..", "alembic.ini"))

class DatabaseManager:
    def __init__(self, settings: DatabaseSettings):
        self._settings = settings
    
    def run_migrations(self):
        print(ALEMBIC_INI_PATH)
        alembic_cfg = config.Config(ALEMBIC_INI_PATH)
        alembic_cfg.set_main_option("sqlalchemy.url", self._settings.url)
        command.upgrade(config=alembic_cfg, revision="head")
    
    async def init_database(self):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.run_migrations)