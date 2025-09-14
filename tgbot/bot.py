import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram.enums import ParseMode


from infrastructure.config import load_config, Config
from tgbot.handlers import routers_list
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.middlewares.database import DatabaseMiddleware
from tgbot.middlewares.messageLogging import LoggingMiddleware
from tgbot.services import services


from infrastructure.database.setup import create_engine
from infrastructure.database.setup import create_session_pool

async def on_startup(bot: Bot, admin_ids: list[int]):
    await services.broadcast(bot, admin_ids, "Бот запущен")


def register_global_middlewares(dp: Dispatcher, config: Config, bot: Bot, session_pool=None):
    """
    Register global middlewares for the given dispatcher.
    Global middlewares here are the ones that are applied to all the handlers (you specify the type of update)

    :param dp: The dispatcher instance.
    :type dp: Dispatcher
    :param config: The configuration object from the loaded configuration.
    :param session_pool: Optional session pool object for the database using SQLAlchemy.
    :return: None
    """
    middleware_types = [
        ConfigMiddleware(config, bot),
        DatabaseMiddleware(session_pool, bot)
    ]
    
    for middleware_type in middleware_types:
        dp.message.outer_middleware(middleware_type)
        dp.callback_query.outer_middleware(middleware_type)
        dp.pre_checkout_query.outer_middleware(middleware_type)

    #Logging only messages, not callback
    dp.message.outer_middleware(LoggingMiddleware(session_pool, bot))
   
    

def setup_logging():
    """
    Set up logging configuration for the application.

    This method initializes the logging configuration for the application.
    It sets the log level to INFO and configures a basic colorized log for
    output. The log format includes the filename, line number, log level,
    timestamp, logger name, and log message.

    Returns:
        None

    Example usage:
        setup_logging()
    """
    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")
   


def get_storage(config):
    """
    Return storage based on the provided configuration.

    Args:
        config (Config): The configuration object.

    Returns:
        Storage: The storage object based on the configuration.

    """
    if config.tg_bot.use_redis:
        return RedisStorage.from_url(
            config.redis.dsn(),
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )
    else:
        return MemoryStorage()


async def main():
    setup_logging()

    

    config = load_config(".env")
    storage = get_storage(config)
    
    db_engine=create_engine(config.db)
    session_pool=create_session_pool(db_engine)

    bot = Bot(token=config.tg_bot.token, parse_mode=ParseMode.HTML)
    
    dp = Dispatcher(storage=storage)
    
    dp.include_routers(*routers_list)

    
    register_global_middlewares(dp, config, bot, session_pool)

    await on_startup(bot, config.tg_bot.admin_ids)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Бот остановлен")
