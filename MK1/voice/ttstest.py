import pyttsx3

# TTS 엔진 초기화
engine = pyttsx3.init()

# 사용 가능한 음성 목록 가져오기
voices = engine.getProperty('voices')



#window + ctrl + n -> 새 음성(선희) 다운 가능.
# 각 음성의 정보 출력
print("\n\n")


for voice in voices:
    print(f"ID: {voice.id} - Name: {voice.name} - Lang: {voice.languages} \n")
