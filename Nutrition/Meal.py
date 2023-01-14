from typing import List, Optional, Sequence, Dict, Any, Tuple

class Meal:
    def __init__(self, meal_id: str, meal_name: str, calories: float, carbs: float, protein: float, fat: float, food: Optional[List[str]] = [], photo: Optional[Sequence[float]] = []):
        self.__meal_id = meal_id
        self.__meal_name = meal_name
        self.__calories = calories
        self.__carbs = carbs
        self.__protein = protein
        self.__fat = fat
        self.__food = food
        self.__photo = photo
    
    @classmethod
    def parse_meal(cls, data: Dict[str, Any]):
        """
        Parses a dictionary of user responses
        -------------------------
        Arguments:
            data (Dict[str, Any]): dictionary of meal data
        -------------------------
        Returns:
            message (str): output message
        """

        meal_id = data["meal_id"] 
        meal_name = cls.__parse_meal_name(meal_id)
        calories = data["calories"]
        carbs = data["carbs"]
        protein = data["protein"]
        fat = data["fat"]
        food = data["food"]

        meal = cls(meal_id, meal_name, calories, carbs, protein, fat, food)
        return meal
    
    def get_meal_id(self) -> str:
        """
        Returns the id of the meal
        """
        return self.__meal_id

    @staticmethod
    def __parse_meal_name(meal_id: int) -> str:
        """
        -------------------------
        Parses the meal name from the meal id
        -------------------------
        Arguments:
            meal_id (int): the id of the meal
        -------------------------
        Returns:
            meal_name (str): meal name    
        """

        meal_number = meal_id + 1
        meal_name = f"Meal {meal_number}"
        
        return meal_name

    def get_all_data(self) -> Tuple[str, float, float, float, float]:
        return self.__meal_name, self.__calories, self.__carbs, self.__protein, self.__fat

    def is_valid(self, meals: List[str]) -> bool: 
        # 1. Check if calories, carbs, protein and fat > 0
        # There are going to be more checks in the future

        return float(self.__calories) > 0 and float(self.__carbs) > 0 and float(self.__protein) > 0 and float(self.__fat) > 0 and self.__meal_id not in meals

    def add_food(self, food: List[str]) -> str:
        pass

    def add_photo(self, photo: Sequence[float]) -> str: 
        pass
