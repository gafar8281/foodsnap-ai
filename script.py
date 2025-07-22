from fastapi import FastAPI, UploadFile, HTTPException, Depends, Query
from starlette import status
from ml_model.model import food_ai_model
from typing import Annotated
from contextlib import asynccontextmanager

from db import models
from db.database import engine, SessionLocal
from sqlalchemy.orm import Session


ml_models = {}
MODEL = 'RestNet50'

@asynccontextmanager
async def lifespan(app: FastAPI):   
    """ Calling Model only Single time"""

    print(f'Loading {MODEL} model')
    ml_models["food_classifier"] = food_ai_model() # code to execute when app is loading
    yield    
    print('Shutting down the model...')  # code to execute when app is shutting down

app = FastAPI(lifespan=lifespan)
models.Base.metadata.create_all(bind=engine)   # CREATE TABLES

# DB CALL
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)] #DEPENDENCY INJECTION



# ENDPOINTS
@app.get('/')
async def project():
    return ({"message": "Food snap Project"})


async def calculate_nutritional_values(quantity, macronutrients):
    """Calculates the nutritional value based on quantity and macronutrients"""

    value = ((macronutrients * 100) * quantity)/100
    return value


@app.post('/foodsnap/v1/upload', status_code= status.HTTP_200_OK)
async def fetch_data(db: db_dependency,image: UploadFile, quantity: int = Query(gt=0)):  
    """ 
    Uploads a food image, classifies it using an ML model, retrieves its nutritional information from the database,
    and calculates the total nutritional values based on the provided quantity.
    
    Returns:
    A dictionary with the food's name, quantity, and calculated calories, carbs, protein, and fats.
    """

    uploaded_image = await image.read()

    try:
        food_name = ml_models["food_classifier"](uploaded_image)
        if not food_name:
            raise ValueError('Food classification failed or returned empty result.')
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return HTTPException(status_code=500, detail='Could not classify the food item. Please try again or with a clearer image')
    
    food_quantity = quantity

    food_data = db.query(models.CalorieNutritionData).filter(models.CalorieNutritionData.dish_name == food_name).first()
    
    if food_data:
        calories = float(food_data.calories)
        carbohydrates = float(food_data.carbohydrates)
        protein = float(food_data.protein)
        fats = float(food_data.fats)

        result = {
            "Dish Name": food_name,
            "Quantity": food_quantity,
            "Calories": f'{await calculate_nutritional_values(food_quantity, calories)}(g)',
            "Carbohydrates" : f'{await calculate_nutritional_values(food_quantity, carbohydrates)}(g)',
            "Protein" : f'{await calculate_nutritional_values(food_quantity, protein)}(g)',
            "Fats" : f'{await calculate_nutritional_values(food_quantity, fats)}(g)' 
        }
        return result    
    else:
        return HTTPException(status_code=404, detail= f"Nutritional data for '{food_name}' could not be found.")




