from flask import Flask
from streetview import street_view
from gpt import gpt

app = Flask(__name__)

# 지도 맞추기
@app.route('/game/guess-location', methods=['GET'])
def guess_location():
    question = "give me 10 longitudes and latitudes of famous tourist spots around the world. the output should be in json with ‘area’, ‘latitude’, ‘longitude’ ‘heading’ as key. the ‘area’ refers to the tourist spot and should be json type. It is crucial the latitude and longitude should not be the exact coordinates, but rather somewhere in the distance where the landmark can be best seen.  Also, the heading refers to the cardinal points which is in range of 0 ~ 360. 360 for north, 180 for south. the heading value should be set to the direction where the spot can be shown on street view from google map. key is area, latitude, longitude, heading."
    response = []
    for location in gpt(question):
        response.append(street_view(location["area"], location["latitude"], location["longitude"], location["heading"]))
    return response

# 얼굴 디즈니화
@app.route('/game/disney-face', methods=['GET'])
def face_merge():
    return 0

# 모여라게임
@app.route('/game/gather-up', methods=['GET'])
def gather_up():
    return 0

if __name__ == '__main__':
    app.run()
