from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

def get_async_session_factory(database_url: str):
    engine = create_async_engine(url=database_url)

    async_session_factory = async_sessionmaker(bind=engine)
    return async_session_factory
