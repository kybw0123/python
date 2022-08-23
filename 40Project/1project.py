import random

random_number = random.randint(1,100)

a = 0
count = 0
while random_number != a:
    try:
        a = input()
        if int(random_number) < int(a):
            print(a, "보다 낮은 숫자를 입력해주세요")
        elif int(random_number) == int(a):
            print("정답입니다!!")
            count = count + 1
            break
        elif int(random_number) > int(a):
            print(a, "보다 높은 숫자를 입력해주세요")
        count = count + 1
    except:
        print('숫자를 입력해주세요')

print("도전 횟수 :",count)
print("게임 종료")

