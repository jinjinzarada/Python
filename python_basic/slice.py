#문자열 슬라이싱 (중요)
str_slice ="0123456789"

print(str_slice[0:7]) 
print(str_slice[0:])
print(str_slice[:10])
print(str_slice[-8:-1])
print(str_slice[-10:])
print(str_slice[0:10:2])
print(str_slice[::-3])
print(str_slice[9::-3])

str_sliceda ="Python"

print(str_sliceda[0:]+str_sliceda[::-1]) #역순
print(str_sliceda[1:5]+str_sliceda[0]+str_sliceda[5])