import tensorflow as tf 
import cv2 as cv
import numpy as np


def food_ai_model(image):
    model = tf.keras.models.load_model('/home/acer/Downloads/indian_food_model.keras')
    # model.summary()

    # image=cv.imread(image, cv.IMREAD_COLOR_RGB)
    img = cv.imdecode(np.frombuffer(image, dtype= np.uint8), cv.IMREAD_COLOR_RGB)    
    image_resized = cv.resize(img, (180,180))
    image = np.expand_dims(image_resized,axis=0)
    # print(image.shape)

    pred = model.predict(image)
    # print(pred)

    class_names = ['adhirasam', 'aloo_gobi', 'aloo_matar', 'aloo_methi', 'aloo_shimla_mirch', 'aloo_tikki', 'anarsa', 'ariselu', 
                   'bandar_laddu', 'basundi', 'bhatura', 'bhindi_masala', 'biryani', 'boondi', 'butter_chicken', 'chak_hao_kheer', 
                   'cham_cham', 'chana_masala', 'chapati', 'chhena_kheeri', 'chicken_razala', 'chicken_tikka', 'chicken_tikka_masala', 
                   'chikki', 'daal_baati_churma', 'daal_puri', 'dal_makhani', 'dal_tadka', 'dharwad_pedha', 'doodhpak', 'dosa', 
                   'double_ka_meetha', 'dum_aloo', 'gajar_ka_halwa', 'gavvalu', 'ghee_rice', 'ghevar', 'grilled_chicken', 'gulab_jamun', 
                   'idli', 'imarti', 'jalebi', 'kachori', 'kadai_paneer', 'kadhi_pakoda', 'kajjikaya', 'kakinada_khaja', 'kalakand', 
                   'karela_bharta', 'kofta', 'kuzhi_paniyaram', 'lassi', 'ledikeni', 'litti_chokha', 'lyangcha', 'maach_jhol', 
                   'makki_di_roti_sarson_da_saag', 'malapua', 'misi_roti', 'misti_doi', 'modak', 'mysore_pak', 'naan', 'navrattan_korma', 
                   'palak_paneer', 'paneer_butter_masala', 'phirni', 'pithe', 'poha', 'poornalu', 'pootharekulu', 'puttu', 'qubani_ka_meetha', 
                   'rabri', 'ras_malai', 'rasgulla', 'rice', 'sandesh', 'shankarpali', 'sheer_korma', 'sheera', 'shrikhand', 'sohan_halwa', 
                   'sohan_papdi', 'sutar_feni', 'unni_appam']

    output_class = class_names[np.argmax(pred)]
    # print("The predicted class is", output_class)
    return output_class
     


# image = '/home/acer/Downloads/archive/Indian Food Images/idli/fbbfimages.jpeg'

# food_ai_model(image)







