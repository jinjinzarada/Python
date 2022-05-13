# 탈출문
# continue 반복문을 생략

numbers = [10, 200, 30, 400, 50]

for i in numbers:
    if i <200:
        continue
    print("{}은 200이상의 숫자입니다.".format(i))

numberss = [[1, 2, 3], [4, 5, 6]]

for i in numberss:
    print(i)
    for j in i:
        print(j)
        break