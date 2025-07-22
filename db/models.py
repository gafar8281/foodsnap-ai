from sqlalchemy import Column, Integer, String
from db.database import Base

class CalorieNutritionData(Base):
    __tablename__ = 'nutrition_data_project'

    id = Column(Integer, primary_key=True, index=True)
    dish_name = Column(String, index= True)
    calories = Column(String)
    carbohydrates = Column(String, default=None)
    protein = Column(String, default=None)
    fats = Column(String, default=None)
    free_sugar = Column(String, default=None)
    fibre = Column(String, default=None)
    sodium = Column(String, default=None)
    calcium = Column(String, default=None)
    iron = Column(String, default=None)
    vitamin_c  = Column(String, default=None)
    folate = Column(String, default=None)


