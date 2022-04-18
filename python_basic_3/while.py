#while문(반복문) 
# i = 0
# num = 0
# print("while 문")
# while i < num:
#     i = i + 1
#     print(i)

# print("if 문")
# if i < num:
#     i = i+1
#     print(i)
num = 0
while num < 5:
    num +=1
    print(num)
else:
    print("값이 {}이상이므로 종료합니다.".format(num))

fruits = ["사과","키위","바나나","사과","망고"]
print(fruits)

fruit = input("빼낼 과일을 입력해주세요 >")

while fruit in fruits:
    fruits.remove(fruit)

print(fruits)
print("{}를 모두 제거했습니다.".format(fruit))