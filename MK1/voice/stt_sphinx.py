import speech_recognition as sr

# Recognizer 객체 생성
recognizer = sr.Recognizer()

# 마이크에서 음성 인식
with sr.Microphone() as source:
    print("말씀해 주세요...")
    
    # 음성을 들을 준비가 되면
    recognizer.adjust_for_ambient_noise(source)
    
    while True:
        try:
            # 음성을 듣기 시작
            audio_data = recognizer.listen(source)
            
            # Sphinx를 사용하여 음성을 텍스트로 변환
            text = recognizer.recognize_sphinx(audio_data,language='ko-KR')
            print("음성 인식 결과:", text)
        
        except sr.UnknownValueError:
            print("Sphinx가 음성을 인식할 수 없습니다.")
        
        except sr.RequestError:
            print("Sphinx에 요청할 수 없습니다.")
        
        except KeyboardInterrupt:
            print("프로그램을 종료합니다.")
            break