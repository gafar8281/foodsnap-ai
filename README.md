# 🥗 FoodSnap AI

**FoodSnap AI** is a lightweight FastAPI application that enables users to obtain nutritional information about food items by simply uploading an image. It uses a pre-trained machine learning model to classify food images and retrieves detailed macronutrient data from a connected database.

---

##  Features

-  **Intelligent Food Classification**  
  Upload an image, and our integrated ResNet50 model identifies the food item.

-  **Comprehensive Nutritional Data**  
  Get calories, carbohydrates, protein, and fats for the identified food.

-  **Quantity-Based Calculations**  
  Receive accurate nutritional values scaled to your specified quantity.

-  **Efficient Model Management**  
  The AI model is loaded once at startup for fast subsequent processing.

-  **Robust API**  
  Exposes a well-structured `/foodsnap/v1/upload` endpoint for seamless integration.

-  **Data Population (Web Scraping)**
  Nutritional data is fetched and updated in the database using web scraping techniques.

  


---

##  Getting Started

Follow the steps below to set up and run **FoodSnap AI** on your local machine.

## Tech Stack

- FastAPI
- TensorFlow
- OpenCV
- SQLAlchemy + PostgreSQL
- Beautiful Soup
- Selenium

##  Installation

```bash
# Clone the repository
git clone https://github.com/your-username/foodsnap-ai.git
cd foodsnap-ai

# Create and activate a virtual environment
python -m venv venv
source venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


