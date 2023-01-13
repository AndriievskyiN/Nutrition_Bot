import numpy as np
from Meal import Meal
from typing import Dict

class Report:
    def __init__(self):
        self.meals = Dict[str, Meal] # { Breakfast: (Meal(...)), Lunch: Meal(...), Dinner: ...}

    def add_meal(self, meal: Meal) -> None:
        if meal.is_valid():
            pass

    def edit_meal(self, meal_id: str) -> None:
        pass

    def remove_meal(self, meal_id: str) -> None:
        pass

    def generate_report(self):
        pass








# 1. send photo : asks whats meal it is
# 2. Choose the button corresponding to the meal
# 3. Send a message e.g. C: 100, which means Carbs = 100
# 4. 

    