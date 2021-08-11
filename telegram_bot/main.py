from aiogram.dispatcher.filters import state
import configs
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
from telegram_buttons import InlineButtons

bot = Bot(configs.TOKEN)
dp = Dispatcher(bot=bot)

ibtns = InlineButtons()
sts = configs.MyState()

@dp.message_handler(commands=['start'])
async def listen(message: Message):
    await message.answer(text="Добро пожаловать в Империю пиццу!")
    await sts.main_options.set()
    return await message.answer(
        text="Ниже вы можете выбрать опции...",
        reply_markup = ibtns.main_options()
        )


@dp.callback_query_handler(state=sts.main_options)
async def operate_main_options(call: CallbackQuery):
    if call.data == "menu":
        await sts.menu.set()
        return await call.message.edit_text(text="Здесь будет меню", reply_markup=ibtns.menu())
    elif call.data == "shares":
        return await call.message.answer(text="Здесь акции")
    elif call.data == "jobs":
        return await call.message.answer(text="Актуальные Вакансии")
    elif call.data == "about":
        return await call.message.answer(text="О компании")


    



if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)

