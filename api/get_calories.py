from flask import *
import requests
def getCalories(filename):
    image = '..\\backend\\images\\' + filename
    api_user_token = 'a800f5691e3eb0db6e04f41ba8debee65b64051d'
    headers = {'Authorization': 'Bearer ' + api_user_token}

    # Single/Several Dishes Detection
    url = 'https://api.logmeal.es/v2/image/segmentation/complete'
    resp = requests.post(url,files={'image': open(image, 'rb')},headers=headers)

    # Nutritional information
    url = 'https://api.logmeal.es/v2/recipe/nutritionalInfo'
    resp = requests.post(url,json={'imageId': resp.json()['imageId']}, headers=headers)
    return resp.json() # return nutritional info