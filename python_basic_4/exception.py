# invalid syntax
# print(구문 오류 내기)
# print("구문 오류 내기")


# IndentationError: expected an indented block
# print(1)

# while True:
#     for i in range(10):
#     print(i)

# print(1)

# while True:
#     for i in range(10):
#         print(i)

# ValueError: invalid literal for int() with base 10
def division():
    num1 = int(input("첫번째 점수를 입력해주세요 >"))
    num2 = int(input("두번째 점수를 입력해주세요 >"))

    return print(f"{num1}을 {num2}로 나눈 값은 {num1/num2}입니다.")

division()

# ValueError, ZeroDivisionError, keyboardInterrupt


# 예외 처리
# try :
#       예외가 발생할 가능성이 있는 코드
# except :
#       예외가 발생했을 때 실행할 코드

def division():
    try:
        num1 = input("첫번째 점수를 입력해주세요 >")
        num2 = input("두번째 점수를 입력해주세요 >")

        return print(f"{num1}을 {num2}로 나눈 값은 {num1/num2}입니다.")
    except Exception:
        print("오류가 발생했습니다.")
    else:
        print("정상적으로 나누기 함수가 호출 되었습니다.")
division()

# help(ValueError)