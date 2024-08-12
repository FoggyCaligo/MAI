import openai

# OpenAI API 키 설정
openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # 사용하고자 하는 GPT 모델
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()