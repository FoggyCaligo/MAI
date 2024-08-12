import speech_recognition as sr

# Recognizer 객체 생성
recognizer = sr.Recognizer()

cmd = ""



# 마이크를 사용하여 음성을 인식
with sr.Microphone() as source:
    print("듣는 중...")

    # 배경 소음을 감지하여 조정
    recognizer.adjust_for_ambient_noise(source)

    # 음성 데이터 수집
    audio_data = recognizer.listen(source)
    try:
        # 구글 음성 인식 API를 사용하여 텍스트로 변환
        text = recognizer.recognize_google(audio_data, language='ko-KR')
        print("음성 인식 결과:", text)
        cmd = text
    except sr.UnknownValueError:
        print("구글 음성 인식 API가 음성을 이해할 수 없습니다.")
    except sr.RequestError as e:
        print(f"구글 음성 인식 API 요청에 실패했습니다; {e}")