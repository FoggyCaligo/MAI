import pyttsx3

# 엔진 초기화
engine = pyttsx3.init()

# 사용 가능한 음성 목록 가져오기
voices = engine.getProperty('voices')

# 'sunhi' 음성을 찾기
for voice in voices:
    if 'sunhi' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        print("found")
        break

# 텍스트를 음성으로 변환
engine.say("안녕하세요, 저는 선희 음성입니다.")
engine.runAndWait()