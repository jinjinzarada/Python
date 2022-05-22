# int(), str(), float(), bool(), tuple()...type()
# 클래스

number = 1
# 1 데이터 int 인스턴스 (객체)
a = 1

# id() = 객체의 주소값을 반환
print(type(number))
print(type(a))
print(type(1))
print(isinstance(number, int))
print(isinstance(a, int))

text1 = 1234
text2 = "1234"

print(id(text1), id(text2))
print(id(text1), id(int(text2)))