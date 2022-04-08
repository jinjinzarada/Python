people = {
    "name": "김영희",
    "phone": "010-1010-2020"
}

print(people["name"],people["phone"])

books = {"Daniel Pink":["파는것이 인간이다.","언제 할 것인가"], "Eric Schidt":"새로운 디지털 시대"}

print(books["Daniel Pink"])

coffee = {"Java":2500,"Amerucano":2500, "Latte":3000}

coffee["Moca"] = 3000

print(coffee)

#요소 삭제
del coffee["Java"]

print(coffee.get("Latte"))
print(coffee.keys())
print(coffee.values())
print(coffee.items())