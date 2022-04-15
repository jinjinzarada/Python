# list[] 안에 ,

list_a =[1,2,3,4]
list_b =["a","b","c"]
list_c = [True,False]
list_d = [1,"a",True]

print(list_a)
print(list_b)
print(list_c)
print(list_d)

numbers = [1,2,3,4,5,6,7]

print(numbers[0])
print(numbers[3:5])
print(numbers[1:])
print(numbers[-3:-1])

list_lan = ["JAVA","C","Python","Go"]

print(list_lan[0][0])
print(list_lan[2][2:4])

list_lan[1] = "C++"

print(list_lan)

list_lan[1:3] = ["C#","Python3"]

print(list_lan)

#list 함수
list_lang = ["JAVA","C","Python","Go"]

print(len(list_lang))
# append() 리스트 맨 뒤에 제일 마지막 인덱스(-1)에 새로운 요소추가

list_lang.append("Ruby")
print(list_lang)

list_a =[1,2,3]
list_lang.append(list_a)

print(list_lang[-1])

#extend() 요소를 추가하는 방법
list_lang.extend(["JavaScript"])

print(list_lang)

# insert(index, data) 
list_lang.insert(0,"R")

print(list_lang)

# Pop() 꺼낸다, remove() 해달 요소 제거,del
list_lang = ["JAVA","C","Python","Go"]

# print(list_lang.pop(5))
# print(list_lang)

list_lang.remove("Python")
print(list_lang)

del list_lang[1]
print(list_lang)

# 숫자,알파벳, 한글
# numbers = [1000,5000,160,100,20,3450]

numbers.sort(reverse= True) # 오름차순으로 정렬 reverse = True 추가해서 내림차순

print(numbers)

# numbers.reverse() # 리스트안에 요소를 역순으로 변경 내림차순은 아님

# print(numbers)

names = ["홍길동","김이박","최횐"]

names.sort(reverse=True)

print(names)
