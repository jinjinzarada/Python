class BreadMold:
    category = "빵"

# 네임스페이스
bread1 = BreadMold()
bread2 = BreadMold()
bread3 = BreadMold()

bread1.price = 3000
bread2.category = "붕어빵"
bread3.category = "잉어빵"

print(bread1.category,bread2.category,bread3.category)

#dir() 이름공간에 있는 모든 속성을 리스트로 반환

# print(dir(bread1))
# print(dir(bread2))
print(dir(str))