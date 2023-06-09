from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from setting import log_setting

from tools.anomaly_generator import generate_path_anomaly
from tools.detections_generator import generate_path_detection
import re

from setting.log_setting import APP_PATH


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
        from project.models import BaseModelClass
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


async def get_database_sql_file_commands():
    lines = ""
    for line in open(f"{APP_PATH}/tools/database.sql").readlines():
        if not line.startswith("--"):
            lines += line + " "

    without_new_lines = re.sub(r"\n", "", lines)
    without_space = re.sub(" +", " ", without_new_lines).strip()
    splitted_queries = without_space.split(";")
    database_sql_file_commands = list(filter(None, splitted_queries))
    return database_sql_file_commands
