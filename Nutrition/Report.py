from Nutrition.Meal import Meal
from typing import Dict, Any

class Report:
    def __init__(self) -> None:
        self.__meals: Dict[int, Meal] = dict() # { Breakfast: (Meal(...)), Lunch: Meal(...), Dinner: ...}
        self.__total_calories: float = 0
        self.__total_carbs: float = 0
        self.__total_protein: float = 0
        self.__total_fat: float = 0

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

        meal_id = meal.get_meal_id()

        if meal.is_valid(list(self.__meals.keys())):
            self.__meals[meal_id] = meal
            return "Meal has been successfully added"
        
        return "There was a problem adding your meal. Try again and make sure all the data is correct"

    def edit_meal(self, meal_id: int, data: Dict[str, Any]) -> str:
        """
        Edits a meal in the report
        -------------------------
        Arguments:
            meal_id (str): The id of the meal to edit
            data (Dict[str, Any]): New data to be set
        -------------------------
        Returns:
            message (str): output message
        """
        
        self.__meals[meal_id] = self.__meals[meal_id].edit_meal(data)
        return "Meal has been sucessfully edited!"

    def remove_meal(self, meal_id: int) -> str:
        """
        Removes a meal to the report
        -------------------------
        Arguments:
            meal_id (str): The id of the meal to remove
        -------------------------
        Returns:
            message (str): output message
        """
        
        del self.__meals[meal_id]
        return "Meal has been successfully removed"

    def clear_report(self) -> str:
        """
        Clears the report
        -------------------------
        Returns:
            message (str): output message
        """

        self.__meals.clear()

        return "The report has been successfully cleared!"


    def get_meal(self, meal_id: int) -> Meal:
        """
        Returns a Meal object from the dictionary of meals
        -------------------------
        Arguments:
            meal_id (int): id of the meal to return
        """

        return self.__meals[meal_id]

    def __reset_totals(self) -> None:
        """
        Resets totals so that when generating a report, the totals aren't accumulated twice
        """

        self.__total_calories = 0
        self.__total_carbs = 0
        self.__total_protein = 0
        self.__total_fat = 0

    def __calculate_totals(self) -> None:
        """
        Updates the total calories, carbs, protein, fat in the report
        """

        for meal in self.__meals.values():
            _, calories, carbs, protein, fat, _ = meal.get_all_data()

            self.__total_calories += calories
            self.__total_carbs += carbs
            self.__total_protein += protein
            self.__total_fat += fat

    def __sort_meals(self) -> None:
        """
        Sorts the meals dictionary by the meal_id
        """

        self.__meals = dict(sorted(self.__meals.items(), key = lambda x: x[0]))

    def generate_report(self) -> str:
        """
        Generates a report 
        
        Returns:
            report (str): output report
        """

        self.__reset_totals()
        self.__calculate_totals()

        # Sort the meals dictionary by meal_id
        self.__sort_meals()

        report = f"-------------------------\nTotal calories: {self.__total_calories}\nTotal carbs: {self.__total_carbs}\nTotal protein: {self.__total_protein}\nTotal fat: {self.__total_fat}"

        for meal in self.__meals.values():
            meal_name, calories, carbs, protein, fat, food = meal.get_all_data()
            food = ", ".join(food) if not food.startswith("pass") else ""

            report += "\n-------------------------"
            report += f"\n{meal_name}:"
            report += f"\nCalories: {calories}"
            report += f"\nCarbs: {carbs}"
            report += f"\nProtein: {protein}"
            report += f"\nFat: {fat}"
            report += f"\nFood: {food}"

        return report 

