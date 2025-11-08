from fastapi import APIRouter, UploadFile, HTTPException, Depends, Form, Request
from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session

from db.database import SessionLocal
from services.nutrition_service import NutritionService


router = APIRouter(prefix="/foodsnap/v1", tags=["foodsnap"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def get_ml_models(request: Request) -> dict:
    return request.app.state.ml_models


@router.get('/', status_code= status.HTTP_200_OK)
async def  project():
    return ({"message": "Foodsnap Project"})

@router.post('/upload', status_code=status.HTTP_200_OK)
async def upload_food_image(db: db_dependency, image: UploadFile, 
                            quantity: int = Form(1, gt=0),
                            ml_models: dict = Depends(get_ml_models)):
    """Upload and classify food image, return nutritional information"""

    uploaded_image = await image.read()

    try:
        food_name = ml_models["food_classifier"](uploaded_image)
        if not food_name:
            raise ValueError('Food classification failed or returned empty result.')
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(
            status_code=500, 
            detail='Could not classify the food item. Please try again or with a clearer image'
        )

    food_data = NutritionService.get_food_nutrition_data(db, food_name)
    print(f"Food name --> {food_name}")
    if not food_data:
        raise HTTPException(
            status_code=404, 
            detail=f"Nutritional data for '{food_name}' could not be found."
        )    

    # Calculate nutritional values
    calories = await NutritionService.calculate_nutritional_values(
        quantity, float(food_data.calories)
    )
    carbohydrates = await NutritionService.calculate_nutritional_values(
        quantity, float(food_data.carbohydrates)
    )
    protein = await NutritionService.calculate_nutritional_values(
        quantity, float(food_data.protein)
    )
    fats = await NutritionService.calculate_nutritional_values(
        quantity, float(food_data.fats)
    )

    nutrition_response = {
            "Dish_Name": food_name,
            "Quantity": quantity,
            "Calories": f'{calories}',
            "Carbohydrates": f'{carbohydrates}(g)',
            "Protein": f'{protein}(g)',
            "Fats": f'{fats}(g)'
        }
    
    print(f"Response: {nutrition_response}")
    return nutrition_response


