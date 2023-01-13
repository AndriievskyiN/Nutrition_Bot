from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from hidden import TOKEN

# Setting up the bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# START COMMAND
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.answer("Hello World!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)