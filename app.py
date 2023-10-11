from flask import Flask
from streetview import street_view
from gpt import gpt
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def guess_location():
    question = "한국에서 유명한 관광지와 그곳의 위도, 경도 하나만 말해줘. 전에 말했던거 제외하고. {'area', 'latitude', 'longitude'}를 key 로 하는 json 형식으로 답해줘. 관광지명은 한국어로."
    json_object = json.loads(gpt(question))
    return street_view(json_object['area'], json_object['latitude'], json_object['longitude'])


if __name__ == '__main__':
    app.run()
