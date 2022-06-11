# 키워드 매개변수

# 키워드 = 특정값 형태로 {"키워드":"특정값"}
def star_player(**kwargs):
    for i, j in kwargs.items():
        if "서장훈" in kwargs.values():
            print("저는 lg팬이라 서장훈을 좋아했어요")
        else:
            print("{}는 역시 {}지".format(i,j))

star_player(농구 = "서장훈")
