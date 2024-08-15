import threading

# 작업 정의
def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)

# 스레드 생성
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# 스레드 시작
t1.start()
t2.start()

# 스레드 완료 대기
t1.join()
t2.join()

print("Threads finished")
