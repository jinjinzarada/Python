# super 부모
# sub 자식

class ParentRestaurant:
    def __init__(self, name, menu, recipe):
        self.name = name
        self.menu = menu
        self.recipe = recipe

    def __str__(self):
        return "가게이름 : {}, 가게의 메뉴 : {}, 메뉴의 조리법 : {}".format(self.name, self.menu,self.recipe)

    def __del__(self):
        pass 

class ChildRestaurant(ParentRestaurant):
    price = 20000
    
    def __init__(self, name, menu, recipe, marketing):
        ParentRestaurant.__init__(self, name, menu, recipe)
        self.marketing = marketing

    def __str__(self):
        return super().__str__() + ", 마케팅 방법 : {}".format(self.marketing)

restaurant_info = ChildRestaurant("자식의 가게","붕어빵","붕어빵을 굽느다.")
print(restaurant_info)

print(issubclass(ChildRestaurant, ParentRestaurant))