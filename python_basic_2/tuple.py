# 여러부분에서 list비슷 
# 요소들을 추가 수정 삭제할수없다. 메모리 저장 공간 적게 사용 빠름
#list[] tuple()

# numbers = (1,) # 한개만할때 끝에 콤마 해주기 꼭!
# append extend 등 사용 불가
# numbers = 1,2,3,4
# numbers = (1,2,3(4,5,6)) 

#언패킹
# numbers = 1,2,3
# 요소보다 많으면(,4) 에러뜸 그럴땐 *number3 
# number1 = numbers[0]
# number2 = numbers[1]
# number3 = numbers[2]
# number1,number2,number3 = numbers

# print(number1, number2, number3)

numbers = 1,2,3,4
print(id(numbers))

numbers += 5,6,
print(id(numbers))


