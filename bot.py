from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper_scripts.hidden import TOKEN
from helper_scripts.InlineKeyboards import Keyboard

# Setting up the bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# START COMMAND
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.answer("Hello World!")

# ADD MEAL
@dp.message_handler(commands=["addmeal"])
async def add_meal(message: types.Message):
    keyboard = Keyboard.meal_id_keyboard()
    await message.answer("Choose the meal", reply_markup=keyboard)

# @dp.callback_query_handler(text=["eng", "ukr", "ru"])
# async def changeLang(call: types.CallbackQuery):

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)