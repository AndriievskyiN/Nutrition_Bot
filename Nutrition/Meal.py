from typing import List, Optional, Sequence, Dict, Any, Tuple

class Meal:
    def __init__(self, meal_id: int, meal_name: str, calories: float, carbs: float, protein: float, fat: float, food: Optional[List[str]] = [], photo: Optional[Sequence[float]] = []):
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
        calories = float(data["calories"])
        carbs = float(data["carbs"])
        protein = float(data["protein"])
        fat = float(data["fat"])
        food = data["food"]

        meal = cls(meal_id, meal_name, calories, carbs, protein, fat, food)
        return meal

    def edit_meal(self, data: Dict[str, Any]):
        """
        Edits the meal
        -------------------------
        Arguments:
            data (Dict[str, Any]): dictionary of new meal data
        -------------------------
        Returns:
            meal (Meal): Meal object with edited data
        """
        
        # self.__meal_id = data["meal_id"] if data["meal_id"] is not None else self.__meal_id
        # # NOTE: MIGHT BLOW UP BECAUSE __parse_meal_name IS A STATIC METHOD
        # self.__meal_name = self.__parse_meal_name(self.__meal_id)

        self.__calories = float(data["calories"]) if not data["calories"].startswith("pass") else self.__calories
        self.__carbs = float(data["carbs"]) if not data["carbs"].startswith("pass") else self.__carbs
        self.__protein = float(data["protein"]) if not data["protein"].startswith("pass") else self.__protein
        self.__fat = float(data["fat"]) if not data["fat"].startswith("pass") else self.__fat
        self.__food = data["food"] if not data["food"].startswith("pass") else self.__food

        return self
    
    def get_meal_id(self) -> int:
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
        return self.__meal_name, self.__calories, self.__carbs, self.__protein, self.__fat, self.__food

    def is_valid(self, meals: List[str]) -> bool: 
        # 1. Check if calories, carbs, protein and fat > 0
        # There are going to be more checks in the future

        return float(self.__calories) > 0 and float(self.__carbs) > 0 and float(self.__protein) > 0 and float(self.__fat) > 0 and self.__meal_id not in meals

    def add_food(self, food: List[str]) -> str:
        pass

    def add_photo(self, photo: Sequence[float]) -> str: 
        pass

    def __repr__(self):
        return f"Meal({self.__meal_id}, {self.__calories}, {self.__carbs}, {self.__protein}, {self.__fat})"

