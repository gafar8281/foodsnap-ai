from fastapi import FastAPI, UploadFile
from starlette import status
from ml_model.model import food_ai_model

app = FastAPI()

@app.get('/')
async def project():

    return ({"message": "Food snap Project"})


@app.post('/foodsnap/v1/upload', status_code= status.HTTP_200_OK)
async def fetch_data(image: UploadFile, quantity: int):

    uploaded_image = await image.read()
    food_name = food_ai_model(uploaded_image)
    food_quantity = quantity

    return ({"name": food_name, "quantity": food_quantity})


