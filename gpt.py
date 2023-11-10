import openai
import json

def gpt(question):
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "'area', 'latitude', 'longitude', 'heading' 를 key 로 하는 json 형식으로 답해줘. 관광지명은 한국어로."},
            {"role": "user", "content": question},
            {"role": "assistant", "content": '{"area": "경복궁", "latitude": 37.579617, "longitude": 126.977041, "heading":90}'},
        ],
        temperature=1,
    )

    json_strings = response['choices'][0]['message']['content'].replace('\n\n', '\n')
    json_list = json.loads(json_strings)
    return json_list

