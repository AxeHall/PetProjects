from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, location
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class InlineButtons:
    def __init__(self) -> None:
        pass
    
    def main_options(self):
        markup = InlineKeyboardMarkup()
        menu = InlineKeyboardButton(text="Меню", callback_data="menu")
        shares = InlineKeyboardButton(text="Акции", callback_data="shares")
        jobs = InlineKeyboardButton(text="Вакансии", callback_data="jobs")
        about = InlineKeyboardButton(text="О нас", callback_data="about")
        markup.add(menu, shares)
        markup.add(jobs, about)
        return markup
    
    def menu(self):
        markup = InlineKeyboardMarkup()
        breakfast = InlineKeyboardButton(text="Завтраки", callback_data="breakfast"),
        pizza_40cm = InlineKeyboardButton(text="Пицца 40 см", callback_data="pizza_40cm")
        rolly = InlineKeyboardButton(text="Роллы", callback_data="rolly")
        salaty = InlineKeyboardButton(text="Салаты", callback_data="salaty")
        zakuski = InlineKeyboardButton(text="Закуски", callback_data="zakuski")
        markup.add(breakfast)
        markup.add(pizza_40cm)
        markup.add(rolly)
        markup.add(salaty)
        markup.add(zakuski)
        return markup


    def breakast(self):
        pass

    def jobs(self):
        markup = InlineKeyboardMarkup()
        waiter = InlineKeyboardButton(text="Официант", callback_data="waiter")
        cook = InlineKeyboardButton(text="Повар", callback_data="cook")
        markup.add(waiter)
        markup.add(cook)
        return markup
""" class TextButtons:
    def __init__(self) -> None:
        pass

    def get_start(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
         """
