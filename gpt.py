import openai
import json

def gpt(a, b, c):
    openai.api_key = ''
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[a, b, c,],
        temperature=1,
    )

    json_strings = response['choices'][0]['message']['content'].replace('\n\n', '\n')
    json_list = json.loads(json_strings)
    return json_list

