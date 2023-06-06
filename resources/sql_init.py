from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .consts import APP_PATH, logger
from .database import get_database_sql_file_commands

from tools.anomaly_generator import generate_path_anomaly
from tools.detections_generator import generate_path_detection


async def init_sqlalchemy(app):
    conf = app["config"]["postgres"]
    app["engine"] = create_async_engine(
        f"postgresql+asyncpg://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['database']}",
        echo=True,
    )
    app["session"] = sessionmaker(
        app["engine"], expire_on_commit=False, class_=AsyncSession
    )

    try:
        await generate_path_anomaly(app)
    except Exception as e:
        logger.error(f"Anomaly generation is not ready yet. Error: {e}")

    try:
        await generate_path_detection(app)
    except Exception as e:
        logger.error(f"Detection generation is not ready yet. Error: {e}")

    try:
        from .database.models import Base
        async with app["engine"].begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database tables created.")
    except Exception as e:
        logger.error(f"Database tables does not created. Error: {e}")

    try:
        async with app["session"]() as session:
            async with session.begin():
                commands = await get_database_sql_file_commands()
                for command in commands:
                    await session.execute(command)
    except Exception as e:
        logger.error(f"Database commands does not created. Error: {e}")

    yield

    await app["engine"].dispose()
