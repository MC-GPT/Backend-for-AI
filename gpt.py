import openai

# 매번 같은 응답이 나오는거 어떻게 처리하지?
def gpt(question):
    openai.api_key = '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'

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 한국 유명 관광지 마스터입니다."},
            {"role": "user", "content": question},
            {"role": "assistant", "content": "한국에서 유명한 관광지와 그곳의 위도, 경도 하나만 말해줘. 전에 말했던거 제외하고."},
        ],
        temperature=1,
    )

    return response['choices'][0]['message']['content']

