from flask import Flask
from streetview import street_view
from gpt import gpt

app = Flask(__name__)

@app.route('/guess-location', methods=['GET'])
def guess_location():
    question = "세계 유명 관광지와 그곳의 위도,경도 말해줘. 10개 말해줘."
    response = []
    for r in gpt(question):
        response.append(street_view(r['area'], r['latitude'], r['longitude']))
    return response

# 얼굴합성
@app.route('/face_merge', methods=['GET'])
def face_merge():
    return 0

# 모여라게임


if __name__ == '__main__':
    app.run()
