from flask import *
import requests
def getCalories(filename):
    image = '.\\images\\' + filename
    api_user_token = 'f5e82c7fb200e4e71ff8b71bcd622745f6e00356'
    headers = {'Authorization': 'Bearer ' + api_user_token}

    # Single/Several Dishes Detection
    url = 'https://api.logmeal.es/v2/image/segmentation/complete'
    resp = requests.post(url,files={'image': open(image, 'rb')},headers=headers)
    # Nutritional information
    url = 'https://api.logmeal.es/v2/recipe/nutritionalInfo'
    # resp = requests.post(url,json={'imageId': resp.json()['imageId']}, headers=headers)
    return resp.json() # return nutritional info