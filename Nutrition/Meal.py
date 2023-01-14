from typing import List, Optional, Sequence

class Meal:
    def __init__(self, meal_id: str, calories: float, carbs: float, protein: float, fat: float, photo: Optional[Sequence[float]] = [], food: Optional[List[str]] = []):
        self.meal_id = meal_id
        self.food = food
        self.photo = photo
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def is_valid(self) -> bool: 
        # 1. Check if calories, carbs, protein and fat > 0
        # There are going to be more checks in the future

        return self.calories > 0 and self.carbs > 0 and self.protein > 0 and self.fat > 0 and self.food != []

    def add_food(self, food: List[str]) -> None:
        pass

    def add_photo(self, photo: Sequence[float]) -> None: 
        pass
