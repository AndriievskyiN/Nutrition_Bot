from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboard:
    def __init__(self, name):
        pass

    @staticmethod
    def meal_id_keyboard():
        buttons = [InlineKeyboardButton(text=f"Meal{i+1}", callback_data=f"meal_{i+1}") for i in range(4)]
        keyboard = InlineKeyboardMarkup().add(*buttons)
        return keyboard






