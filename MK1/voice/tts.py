import pyttsx3


# TTS 엔진 초기화
engine = pyttsx3.init()

# 음성 설정 (선택 사항)
engine.setProperty('rate', 150)    # 음성 속도 설정
engine.setProperty('volume', 1)    # 볼륨 설정 (0.0 to 1.0)

# # 텍스트를 음성으로 변환
# text = "테스트"
# engine.say(text)

# # 음성 재생
# engine.runAndWait()




def say(str):
    engine.say(str)
    engine.runAndWait()
    
def stop():
    engine.stop()
    

say("테스트")
# stop()