# 탈출문
# break 반복문을 중단

i=0

while True:
    print("{}번째 반복입니다.".format(i))
    i += 1
    if i > 10: 
        break

sum_= 0

while True:
    num = int(input("정수를 입력해주세요(0입력시 종료) > "))
    # if num == 0:
    #     break
    sum_+= num
    print("현재 정수의 합은 {}입니다.".format(sum))
else:
    print("반복문이 종료되었습니다.")