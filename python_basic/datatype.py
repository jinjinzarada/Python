# int(정수)형

a = 5
b = -5
c = 0

print(type(a), type(b),type(c))

# #float(실수)형

d = 5.5
e = -5.5
f = 0.0

print(type(d), type(e), type(f))

# #과학적 표기법

g = 1.234567e5

print(g)

#complex 자료형
################################
text = "String \"Data\" Type"

print(text)

#탈출문자
#\', \",\\, \n, \r, \t

text = "Python \'is\" Easy"
text = "Python \\is\\ Easy"
text = "Python \n is Easy"
text = "Java \rPython is Easy"
text = "\tPython is Easy"
text = "P\tython is Easy"
text = '''Python
is
Easy'''
text2 = "and Powerful"

print(text+text2)
################################
a = 10 
b = 20

print(a, b, sep='곱하기 2는')
print(a, b, end='\t')
print("3번째 라인!")
################################
#bool형 논리연산을 이용해서 여러개의 명제를
#하나로 조합하거나 명제를 부정

is_true = True
is_false = False

print(is_false)
# false : 거짓이거나 0에 해당하는 값, 빈 문자,[](){},null