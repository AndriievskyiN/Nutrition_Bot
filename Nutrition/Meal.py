from typing import List, Optional, Sequence, Dict, Any

class Meal:
    def __init__(self, meal_id: str, calories: float, carbs: float, protein: float, fat: float, food: Optional[List[str]] = [], photo: Optional[Sequence[float]] = []):
        self._meal_id = meal_id
        self._calories = calories
        self._carbs = carbs
        self._protein = protein
        self._fat = fat
        self._food = food
        self._photo = photo
    
    @staticmethod
    def parse_meal(data: Dict[str, Any]) -> str:
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
        calories = data["calories"]
        carbs = data["carbs"]
        protein = data["protein"]
        fat = data["fat"]
        food = data["food"]

        return Meal(meal_id, calories, carbs, protein, fat, food)

    def _is_valid(self) -> bool: 
        # 1. Check if calories, carbs, protein and fat > 0
        # There are going to be more checks in the future

        return self.calories > 0 and self.carbs > 0 and self.protein > 0 and self.fat > 0

    def add_food(self, food: List[str]) -> str:
        pass

    def add_photo(self, photo: Sequence[float]) -> str: 
        pass
