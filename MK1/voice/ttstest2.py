import pyttsx3
import asyncio

engine = pyttsx3.init()

async def speak(text):
    engine.say(text)
    engine.runAndWait()

async def main():
    text = "This is a sample text that will be spoken by pyttsx3."
    task = asyncio.create_task(speak(text))
    
    await asyncio.sleep(0.1)  # 2초 대기
    engine.stop()  # 2초 후 음성 출력 중지

    await task

asyncio.run(main())