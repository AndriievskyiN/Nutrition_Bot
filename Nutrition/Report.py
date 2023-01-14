from Nutrition.Meal import Meal
from typing import Dict

class Report:
    def __init__(self) -> None:
        self._meals = Dict[str, Meal] # { Breakfast: (Meal(...)), Lunch: Meal(...), Dinner: ...}

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

        meal_id = meal["meal_id"]

        if meal.is_valid():
            self.meals[meal_id] = meal
            return "Meal has been successfully added"

        self.meals[meal_id] = meal
        
        return "There was a problem adding your meal. Make sure all the data is correct"

    def edit_meal(self, meal_id: str) -> str:
        """
        Edits a meal in the report
        -------------------------
        Arguments:
            meal_id (str): The id of the meal to edit
        -------------------------
        Returns:
            message (str): output message
        """
        pass

    def remove_meal(self, meal_id: str) -> str:
        """
        Removes a meal to the report
        -------------------------
        Arguments:
            meal_id (str): The id of the meal to remove
        -------------------------
        Returns:
            message (str): output message
        """
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
        """
        Generates a report 
        -------------------------
        Returns:
            report (str): output report
        """
        pass