# 지역변수(local variable), 전역변수(global variable)

# 지역변수
# def jeju_potato(potato):
#     potato = "고구마"
#     print(potato)

# jeju_potato()

# 전역변수 한번만 선언해서 계속할 수 있다 함수 
# potato = "감자"

# def jeju_potato():
#     potato = "고구마"
#     print(potato)

# print(potato)
# jeju_potato()

a , b = 20, 40

def add(num1, num2 = 20, num3 = 30):
    return num1 + num2 + num3

a,b = 5, 10

print(add(a, b))

def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(10, 20, 30, 40)