from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from db import models
from db.database import engine
from routes import foodsnap
from ml_model.model import food_ai_model

# Global model storage
ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):   
    """ Calling Model only Single time"""

    print(f'\nLoading {settings.MODEL_NAME} model')
    ml_models["food_classifier"] = food_ai_model() # code to execute when app is loading
    # expose models on app state for access within routes
    app.state.ml_models = ml_models  
    yield    
    print('\nShutting down the model...')  # code to execute when app is shutting down

#FastAPI app
app = FastAPI(
    title="FoodSnap AI",
    description="AI-powered food classification and nutrition analysis",
    version="1.0.0",
    lifespan=lifespan
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins= settings.CORS_ORIGINS,
    allow_credentials=True,  # Allow cookies and authorization headers
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],     # Allow all headers in the request
)

# router
app.include_router(foodsnap.router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)


