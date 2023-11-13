from flask import Flask, request
from streetview import street_view
from gpt import gpt

app = Flask(__name__)

# 조명 gpt
@app.route('/appliance/gpt', methods=['POST'])
def app_gpt():
    request_data = request.get_json()
    mood_data = request_data.get('mood', '')
    question = "Generate one RGB value suitable for a home party with about 20 people. output should be json with 'color_code' and color_code like #0000. I prefer" + mood_data + "mood."
    a = {"role": "system", "content": "'color_code' 를 key 로 하는 json 형식으로 답해줘."}
    b = {"role": "user", "content": question}
    c = {"role": "assistant", "content": '{"color": "#9B59B6"}'}
    return gpt(a, b, c)

# 지도 맞추기
@app.route('/game/guess-location', methods=['GET'])
def guess_location():
    question = "give me 10 longitudes and latitudes of famous tourist spots around the world. the output should be in json with ‘area’, ‘latitude’, ‘longitude’ ‘heading’ as key. the ‘area’ refers to the tourist spot and should be json type. It is crucial the latitude and longitude should not be the exact coordinates, but rather somewhere in the distance where the landmark can be best seen.  Also, the heading refers to the cardinal points which is in range of 0 ~ 360. 360 for north, 180 for south. the heading value should be set to the direction where the spot can be shown on street view from google map. key is area, latitude, longitude, heading."
    a = {"role": "system", "content": "'area', 'latitude', 'longitude', 'heading' 를 key 로 하는 json 형식으로 답해줘. 관광지명은 한국어로."}
    b = {"role": "user", "content": question}
    c = {"role": "assistant", "content": '{"area": "경복궁", "latitude": 37.579617, "longitude": 126.977041, "heading":90}'}
    response = []
    for location in gpt(a, b, c):
        response.append(street_view(location["area"], location["latitude"], location["longitude"], location["heading"]))
    return response

# 얼굴 디즈니화
@app.route('/game/disney-face', methods=['GET'])
def disney_face():
    response = []
    url = "https://mc-nugu.s3.ap-northeast-2.amazonaws.com/"
    name_list = ["수지", "아이유", "윈터", "장원영", "제니", "해린", "윈터", "카리나"]

    for i, item in enumerate(name_list):
        response.append({"quiz": url + "quiz/" + str(i) + ".png", "answer": url + "answer/" + str(i) + ".jpg", "name": name_list[i]})

    return response

# 모여라게임
@app.route('/game/gather-up', methods=['GET'])
def gather_up():
    return 0

if __name__ == '__main__':
    app.run()
