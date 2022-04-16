# Add 123,"문자",True, ("튜플")은 추가기능

week = {"월요일","화요일","수요일","목요일","금요일","토요일","일요일"}
week.update(["일주일",],{"한달":123}) 
# 키만 추가됨

# a = {0, "abc", False}
# a.add(1)

print(week)

#집합
week = set(["월요일","화요일","수요일","목요일","금요일","토요일","일요일"])

print(week)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
# 합집합
print(a | b)
# 교집합
print(a & b)
# 차집합
print(a - b)
# 원소들 삭제
a.remove(4)
print(a)
a.remove(True)
print(a)