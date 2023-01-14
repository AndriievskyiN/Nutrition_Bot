from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboard:
    def __init__(self, name):
        pass

    @staticmethod
    def meal_id_keyboard(n_buttons=4):
        buttons = [InlineKeyboardButton(text=f"Meal {i+1}", callback_data=i) for i in range(n_buttons)]
        keyboard = InlineKeyboardMarkup().add(*buttons)
        return keyboard






