from db import models
from sqlalchemy.orm import Session
# from typing import Dict, Any


class NutritionService:
    @staticmethod
    async def calculate_nutritional_values(quantity: int, macronutrients: float) -> float:
        """Calculates the nutritional value based on quantity and macronutrients"""
        value = ((macronutrients * 100) * quantity)/100
        return value

    @staticmethod
    def get_food_nutrition_data(db: Session, food_name: str):
        """Retrieve nutrition data for a food item"""

        nutri_values = db.query(models.CalorieNutritionData).filter(models.CalorieNutritionData.dish_name == food_name).first()
        return nutri_values



