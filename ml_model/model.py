import tensorflow as tf 
import cv2 as cv
import numpy as np


def food_ai_model():
    model = tf.keras.models.load_model(r'c:\Users\GAFAR\Downloads\food_model.keras')

    def predict_food_name(image):
        # image=cv.imread(image, cv.IMREAD_COLOR_RGB)
        img = cv.imdecode(np.frombuffer(image, dtype= np.uint8), cv.IMREAD_COLOR_RGB)    
        image_resized = cv.resize(img, (180,180))
        image = np.expand_dims(image_resized,axis=0)

        pred = model.predict(image)

        class_names = ['adhirasam', 'aloo matar', 'aloo shimla mirch', 'aloo tikki', 'anarsa', 'apple fruit', 'ariselu',
                        'banana fruit', 'bandar laddu', 'basundi', 'bhatura', 'bhindi masala', 'biryani', 'boiled egg',
                        'boiled rice', 'boondi raita', 'butter chicken', 'carrot', 'cauliflower', 'cham cham',
                        'chana masala', 'chapati', 'cheese pizza', 'chicken stew', 'chicken tikka', 'chicken tikka masala',
                        'chikki', 'daal baati churma', 'daal puri', 'dal makhani', 'dal tadka', 'dharwad pedha', 'doodhpak',
                        'double ka meetha', 'dum aloo', 'fish curry', 'gajar ka halwa', 'gavvalu', 'ghee rice', 'ghevar',
                        'gobi 65', 'gulab jamun with khoya', 'hot tea', 'idli', 'imarti', 'jalebi', 'kachori', 
                        'kadhi pakoda', 'kajjikaya', 'kakinada khaja', 'kalakand', 'karela bharta', 'kofta', 
                        'kuzhi paniyaram', 'lassi', 'litti chokha', 'makki ki roti', 'malapua', 'misti doi', 'modak', 
                        'mysore pak', 'naan', 'navrattan korma', 'orange fruit', 'palak paneer', 'paneer butter masala', 
                        'pea paneer curry', 'phirni', 'pithe', 'plain dosa', 'poha', 'poornalu', 'pootharekulu', 'rabri', 
                        'ras malai', 'rasgulla', 'rice puttu', 'sandesh', 'shankarpali', 'sheer korma', 'sheera', 'shrikhand', 
                        'sohan halwa', 'sohan papdi', 'tandoori chicken', 'tomatoes', 'unni appam']


        output_class = class_names[np.argmax(pred)]
        return output_class
    
    return predict_food_name
     









