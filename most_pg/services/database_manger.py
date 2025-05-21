from ..settings import DatabaseSettings
from alembic import command, config
import asyncio
import most_pg
from importlib import resources

class DatabaseManager:
    def __init__(self, settings: DatabaseSettings):
        self._settings = settings
    
    def run_migrations(self):
        with resources.as_file(resources.files(most_pg) / "alembic.ini") as ini_file, \
            resources.as_file(resources.files(most_pg) / "alembic") as alembic_dir:
            alembic_cfg = config.Config(str(ini_file))
            alembic_cfg.set_main_option("script_location", str(alembic_dir))
            alembic_cfg.set_main_option("sqlalchemy.url", self._settings.url)
            command.upgrade(config=alembic_cfg, revision="head")
    
    async def init_database(self):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.run_migrations)