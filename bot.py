from aiogram import Bot, Dispatcher
import handlers


async def main() -> None:
    BOT_TOKEN: str = "6913302359:AAF6DEMgogjHS3MVyBv95w9LbUac06Z3fXc"

    bot: Bot = Bot(token=BOT_TOKEN)

    dp: Dispatcher = Dispatcher(
        bot=bot)

    dp.include_router(handlers.start.router)
    dp.include_router(handlers.user_handler.router)

    await dp.start_polling(bot)
