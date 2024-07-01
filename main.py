import asyncio
import logging

from aiogram import Bot, Dispatcher


# Запуск процесса поллинга новых апдейтов
async def main():
    logging.basicConfig(level=logging.INFO)  # Включаем логирование, чтобы не пропустить важные сообщения

    # Если умеешь пользоваться с скрытыми данными, то я всё накидал в System_files/Config
    bot = Bot(token=config.bot_token.get_secret_value())  # Объект бота
    # Если не умеешь, то просто вставляй токен бота после token=
    dp = Dispatcher()

    dp.include_router(Start_router.router)  # Импортируешь модуль и вставляешь его в скобках как на данном примере

    await bot.delete_webhook(drop_pending_updates=True)  # Удаление вебхуков (что бы не срабатывали те, когда бот не работал)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
