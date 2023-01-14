from Nutrition.Meal import Meal
from typing import Dict

class Report:
    def __init__(self):
        self.meals = Dict[str, Meal] # { Breakfast: (Meal(...)), Lunch: Meal(...), Dinner: ...}

    def add_meal(self, meal: Meal) -> str:
        """
        Adds a meal to the report
        -------------------------
        Arguments:
            meal (Meal): Meal object
        -------------------------
        Returns:
            message (str): output message
        """

        if meal.is_valid():
            self.meals[meal.meal_id] = meal
            return "Meal has been successfully added"
        
        return "There was a problem adding your meal. Make sure all the data is correct"

    def edit_meal(self, meal_id: str) -> str:
        pass

    def remove_meal(self, meal_id: str) -> str:
        pass

    def clear_report(self) -> str:
        """
        Clears the report
        -------------------------
        Returns:
            message (str): output message
        """

        self.meals.clear()

        return "The report has been successfully cleared!"

    def generate_report(self) -> str:
        pass