from flask import *
import openai
import os
import io
import base64
from PIL import Image
from io import BytesIO
from api.get_calories import getCalories

app = Flask(__name__)
openai.api_key = "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"

@app.route("/getData", methods=['GET', 'POST'])
def getSugestion():
    file = request.files['file']
    file.save(os.path.join('..\\backend\\images', file.filename))
    calorieCalculated = getCalories(file.filename)['nutritional_info']['calories']
    GENDER = 'Male'
    BMI = 24.9
    AGE = 50
    result = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages= [{'role': 'user', 'content': 'Amount of calories required for a {} person with {} and age {} per day. The current food has {} calories. Is it good to have this amount of calorie by not considering amount of calories the person already took. Please provide ways to get required amount of calorie in a day. Don\'t specify you are an AI model. The result should focus on the calorie currently took by the person and the data should be short and up to the point. No need of summary'.format(GENDER, BMI, AGE, calorieCalculated)}],
    temperature=0)
    image = getImage('..\\backend\\images')
    response = {
        'result': result["choices"][0]["message"]["content"],
        'image': image
    }
    return jsonify(response)

def getImage(filePath):
    image = Image.open(filePath, mode='r')
    imgByteArr = io.BytesIO()
    imgByteArr = imgByteArr.getvalue()
    imgByteArr = base64.encodebytes(imgByteArr).decode('ascii')
    return image
