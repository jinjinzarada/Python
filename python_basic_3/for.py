# for문 
# for 변수 in 나열가능한 자료:
#    실행할 문장
# for i in range(1, 10+1):
#     print(i)

# for i in "일이삼사오":
#     print(i)

# fruits = ["사과","딸기","바나나"]
# for i in fruits:
#     print("과일 바구니에 {}가 들어있습니다.".format(i))

# 1부터 30까지의 수 중에서 3의 배수들의 합을 구하시오.
# 3의 배수는 어떻게 구하면 될까
# % 3 ==0
sum = 0

# for i in range(1,30+1):
#     if i % 3== 0:
#         print("{} + {} =".format(sum, i), end = "")
#         sum += i
# print(sum)

for i in range(3,30+1, 3):
    print("{} + {} =".format(sum, i), end = "")
    sum += i
print(sum)

coffee = {"아메리카노" : 2500, "라떼" : 3000, "자바" : 2500}

for i in coffee.items():
    print(i)

fruits = ["사과", "딸기","바나나"]

for i in enumerate(fruits):
    print(f"{i[0]+1}번째 과일은 {i[1]}입니다.")

for i,j in enumerate(fruits):
    print(f"{i+1}번째 과일은 {j}입니다.")