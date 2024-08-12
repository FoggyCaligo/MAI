import pyttsx3
import threading
import time

class TTSManager:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.speaking = False
        self.thread = None

        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',voices[0].id)


    def speak(self, text):
        if self.thread and self.thread.is_alive():
            self.stop_speech()

        self.speaking = True
        self.thread = threading.Thread(target=self._speak, args=(text,))
        self.thread.start()

    def _speak(self, text):
        def on_end(name, completed):
            self.speaking = False
        
        self.engine.connect('finished-utterance', on_end)
        self.engine.say(text)
        self.engine.runAndWait()

    def stop_speech(self):
        if self.speaking:
            self.engine.stop()
            self.speaking = False




# 사용 예시
tts = TTSManager()

# 음성 시작
tts.speak("파이썬 tts 작동중 정지 코드 테스트")
# 잠시 기다린 후 중지
time.sleep(1)
tts.stop_speech()