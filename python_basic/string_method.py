# 내장함수 : print() - 괄호 안에 인자를 넣어서 사용
# 메서드 : .upper() - (참조연산자)를 이용해서 특정한 데이터를 참조해서 사용

# text = "www.GOOGLE.com"
#leg(length) # 문자열의 길이를 반환
# print(len(text))

# #capitalize : 첫문자를 대문자로
# txt_capitalize = text.capitalize()

# print(txt_capitalize)

# txt_upper=text.upper() # 문자열 전체를 대문자로 변경
# txt_lower=text.lower() # 문자열 전체를 소문자로 변경

# print(txt_upper)
# print(txt_lower)

# # count, find, index 

# g_cnt = text.count('GO') # 찾는 문자의 갯수를 반환
# g_cnt = text.count('X')
# print(g_cnt)

# g_find = text.find('G')
# g_find = text.find('G',5)
# g_find = text.find('X')
# g_idx = text.index('X')
# g_find = text.rfind('G')
# g_find = text.rindex('G')
# print(g_find) # 찾는 문자의 인덱스를 반환
# print(g_idx) # 찾는 문자의 인덱스를 반환 
#text_naver = text.replace("GOOGLE","NAVER") # 문자열 치환
# text.split('OO') # 문자열을 분리 

# print(text_naver)

text ="         www.GOOGLE.com          "

print(text)
stp=text.strip() # 공백 제거 그러나 w w w 이런식은 공백제거안됨
print(stp)