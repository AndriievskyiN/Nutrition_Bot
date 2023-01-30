from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from helper_scripts.hidden import TOKEN
from Nutrition.Meal import Meal
from Nutrition.Report import Report
from helper_scripts.InlineKeyboards import Keyboard
from dialogs import MealHandler
from input_validator import InputValidator

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
@dp.message_handler(commands=["addmeal", "editmeal"])
async def add_meal(message: types.Message, state: FSMContext):
    keyboard = Keyboard.meal_id_keyboard()

    await message.answer("Choose the meal", reply_markup=keyboard)
    await state.update_data(
       {"command": message.text}
    )   

    await MealHandler.meal_id.set()

@dp.callback_query_handler(text=[i for i in range(4)], state=MealHandler.meal_id)
async def get_meal_id(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()

    data = await state.get_data()
    command = data["command"]

    meal_id = int(call.data)
    await state.update_data(
        {"meal_id": meal_id}
    )


    if command == "/addmeal":
        await call.message.answer("Great! What is the amount of calories you have eaten?")
    
    elif command == "/editmeal":
        await call.message.answer("What is the new amount of calories you have eaten? \nType \"pass\" not to change it")

    await MealHandler.next()

@dp.message_handler(state=MealHandler.calories)
async def get_calories(message: types.Message, state: FSMContext):
    value = message.text
    data = await state.get_data()
    command = data["command"]
    
    if not InputValidator.is_valid_number(value, command):
        await message.answer("The data you entered is invalid... Try again and make sure everything is good")
        await state.finish()
        # await MealHandler.previous()
        # await add_meal(message, state)

    else:
        calories = value
        await state.update_data(
            {"calories": calories}
        )

        if command == "/addmeal":
            await message.answer("Great! What is the amount of carbs you have eaten?")

        elif command == "/editmeal":
            await message.answer("What is the new amount of carbs you have consumed? \nType \"pass\" not to change it")

        await MealHandler.next()

@dp.message_handler(state=MealHandler.carbs)
async def get_carbs(message: types.Message, state: FSMContext):
    value = message.text
    data = await state.get_data()
    command = data["command"]

    if not InputValidator.is_valid_number(value, command):
        await message.answer("The data you entered is invalid... Try again and make sure everything is good")
        await state.finish()

    else:
        carbs = value
        await state.update_data(
            {"carbs": carbs}
        )

        if command == "/addmeal":
            await message.answer("Great! What is the amount of protein you have eaten?")

        elif command == "/editmeal":
            await message.answer("What is the new amount of protein you have consumed? \nType \"pass\" not to change it")
        await MealHandler.next()

@dp.message_handler(state=MealHandler.protein)
async def get_protein(message: types.Message, state: FSMContext):
    value = message.text
    data = await state.get_data()
    command = data["command"]
    
    if not InputValidator.is_valid_number(value, command):
        await message.answer("The data you entered is invalid... Try again and make sure everything is good")
        await state.finish()

    else:
        protein = value
        await state.update_data(
            {"protein": protein}
        )

        if command == "/addmeal":
            await message.answer("Great! What is the amount of fat you have eaten?")
        
        elif command == "/editmeal":
            await message.answer("What is the new amount of fat you have consumed? \nType \"pass\" not to change it")
        await MealHandler.next()

@dp.message_handler(state=MealHandler.fat)
async def get_fat(message: types.Message, state: FSMContext):
    value = message.text
    data = await state.get_data()
    command = data["command"]
    
    if not InputValidator.is_valid_number(value, command):
        await message.answer("The data you entered is invalid... Try again and make sure everything is good")
        await state.finish()

    else:
        fat = value
        await state.update_data(
            {"fat": fat}
        )

        if command == "/addmeal":
            await message.answer("Lastly, what food have you eaten? \nType each food item seperated by a comma (e.g. rice, chicken, salad) \nType \"pass\" to skip this part")
        elif command == "/editmeal":
            await message.answer("Lastly, what new food have you consumed? \nType each food item seperated by a comma (e.g. rice, chicken, salad) \nType \"pass\" not to change it")
        await MealHandler.next()

@dp.message_handler(state=MealHandler.food)
async def get_food(message: types.Message, state: FSMContext):
    food = message.text if message.text.startswith("pass") else [i for i in message.text.split(",")]
    await state.update_data(
        {"food": food}
    )

    # Get meal data
    data = await state.get_data()
    command = data["command"]

    if command == "/addmeal":
        # Add meal to the report
        meal = Meal. parse_meal(data)
        output_message = report.add_meal(meal)

    elif command == "/editmeal":
        meal_to_edit = data["meal_id"]
        output_message = report.edit_meal(meal_to_edit, data)

    await message.answer(output_message)
    await state.finish()

# GENERATE REPORT
@dp.message_handler(commands=["getreport"])
async def get_report(message: types.Message):
    generated_report = report.generate_report()
    await message.answer(generated_report)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)