import threading
import time

# 2가지 동작이 동시에 실행되는 코드 만들고 실행
'''
def thread_1():
    while True:
        print('쓰레드1 동작')
        time.sleep(1)

t1 = threading.Thread(target=thread_1)
t1.start()

while True:
    print('메인 동작')
    time.sleep(2)
'''
#
# # 메인코드가 동작할 때에만 쓰레드 동작하는 코드 만들기
# def thread_1():
#     while True:
#         print('쓰레드1 동작')
#         time.sleep(1)
#
# t1 = threading.Thread(target=thread_1)
# t1.daemon = True
# t1.start()
#
# while True:
#     print('메인동작')
#     time.sleep(2)

# 다수의 쓰레드를 동작시키는 코드 만들고 실행
def sum(name, value):
    for i in range(0, value):
        print(f'{name} : {i}')

t1 = threading.Thread(target=sum, args=('1번 쓰레드', 10))
t2 = threading.Thread(target=sum, args=('2번 쓰레드', 10))
t1.start()
t2.start()

print('Main Thread')