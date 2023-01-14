from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from helper_scripts.hidden import TOKEN
from Nutrition.Meal import Meal
from Nutrition.Report import Report
from helper_scripts.InlineKeyboards import Keyboard
from meal_handler import MealHandler

# Setting up the bot
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Initialize the report
report = Report()

# START COMMAND
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.answer("Hello World!")

# ADD MEAL
@dp.message_handler(commands=["addmeal"])
async def add_meal(message: types.Message):
    keyboard = Keyboard.meal_id_keyboard()
    await message.answer("Choose the meal", reply_markup=keyboard)
    await MealHandler.meal_id.set()


@dp.callback_query_handler(text=[f"meal_{i}" for i in range(4)], state=MealHandler.meal_id)
async def get_meal_id(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    meal_id = call.data
    await state.update_data(
        {"meal_id": meal_id}
    )

    await call.message.answer("Great! What is the total amount of calories you have eaten?")
    await MealHandler.next()

@dp.message_handler(state=MealHandler.calories)
async def get_calories(message: types.Message, state: FSMContext):
    calories = message.text
    await state.update_data(
       {"calories": calories}
    )

    await message.answer("Great! What is the amount of carbs you have eaten?")
    await MealHandler.next()

@dp.message_handler(state=MealHandler.carbs)
async def get_carbs(message: types.Message, state: FSMContext):
    carbs = message.text
    await state.update_data(
       {"carbs": carbs}
    )

    await message.answer("Great! What is the amount of protein you have eaten?")
    await MealHandler.next()

@dp.message_handler(state=MealHandler.protein)
async def get_protein(message: types.Message, state: FSMContext):
    protein = message.text
    await state.update_data(
       {"protein": protein}
    )

    await message.answer("Great! What is the amount of fat you have eaten?")
    await MealHandler.next()

@dp.message_handler(state=MealHandler.fat)
async def get_fat(message: types.Message, state: FSMContext):
    fat = message.text
    await state.update_data(
       {"fat": fat}
    )

    await message.answer("Lastly, what food have you eaten? \nType each food item seperated by a comma (e.g. rice, chicken, salad) \nType \"pass\" to skip this part")
    await MealHandler.next()

@dp.message_handler(state=MealHandler.food)
async def get_food(message: types.Message, state: FSMContext):
    if message.text.lower() == "pass":
        await state.update_data(
            {"food": None}
        )

    else:  
        food = [i for i in message.text.split(",")]
        await state.update_data(
            {"food": food}
        )

    data = await state.get_data()
    meal = Meal.parse_meal(data)
    report.add_meal(meal)

    await message.answer("Amazing! All data has been added!")
    await state.finish()

# @dp.message_handler(state=MealHandler.photo)
# async def get_data(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     print(data)
#     await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)