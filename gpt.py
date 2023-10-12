import openai
import json

def gpt(question):
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "'area', 'latitude', 'longitude' 를 key 로 하는 json 형식으로 답해줘. 관광지명은 한국어로."},
            {"role": "user", "content": question},
            {"role": "assistant", "content": '{"area": "경복궁", "latitude": 37.579617, "longitude": 126.977041}'},
        ],
        temperature=1,
    )

    # 데이터를 "\n"으로 분할하여 JSON 객체 목록을 얻습니다.
    json_strings = response['choices'][0]['message']['content'].replace('\n\n', '\n')
    json_strings = json_strings.split("\n")
    json_list = []
    for item in json_strings:
        item = item.strip()
        json_obj = json.loads(item)
        json_list.append(json_obj)
    print(json_list)
    return json_list

