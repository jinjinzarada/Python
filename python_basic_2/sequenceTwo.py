list_lang = ["JAVA","C","Python","Go"]
numbers = [1,200,3,50,5,66,7,55,9]

# in연산자와 not in 연산자

print(50 in numbers)
print("C" in list_lang)
print("Java script" not in list_lang)

#index 이해
# 0 1 2 3
#  가나다
#-3-2-1 0

text =["가","나","다"]

print(text[0])
print(text[1])
print(text[2])

print(text[-1])
print(text[-2])
print(text[-3])

print(text[1:2])

# 이차원 list 표 모양이라 생각하면 됨.
td_number =[[10,20,30],[1,2,3]] #2행 3열

print(td_number[1])
print(td_number[0][0]) #처음[행] 두번째[열]
print(td_number[1][2])
print(td_number[0][0:2])