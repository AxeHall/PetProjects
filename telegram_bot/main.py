import configs
from aiogram import Bot, Dispatcher, executor

bot = Bot(configs.TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler()
async def parrot(message):
    if "привет" in message.text.lower() or "здравствуйте" in message.text.lower():
        return await message.answer(text="Здравствуйте, чем могу помочь?")
    elif "как дела" in message.text.lower():
        return await message.answer(text="Хорошо, как у вас?")
    elif june_21.get(message.text.lower()):
        return await message.answer(text=june_21.get(message.text.lower()))
    else:
        return await message.answer(text="Простите, я Вас не совсем понял!")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
