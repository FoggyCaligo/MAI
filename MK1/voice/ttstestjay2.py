import pyttsx3
import threading
import time

engine = pyttsx3.init()

def speak(str):
    engine.say(str)
    engine.runAndWait()

def stopspkMnger():
    time.sleep(1)
    engine.stop()


# 스레드 생성
t1 = threading.Thread(target=speak("파이썬 tts 작동중 정지  테스트"))
t2 = threading.Thread(target=stopspkMnger)

# 스레드 시작
t1.start()
t2.start()

# 스레드 완료 대기
t1.join()
t2.join()

print("Threads finished")
