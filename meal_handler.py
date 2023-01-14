from aiogram.dispatcher.filters.state import StatesGroup, State

class MealHandler(StatesGroup):
    meal_id = State()
    calories = State()
    carbs = State()
    protein = State()
    fat = State()
    food = State()
    photo = State()