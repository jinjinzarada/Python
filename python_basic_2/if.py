# if True:
#     print("실행할 문장입니다.")
# 조건식이 참일 때 실행할 문장
# if 공백 4칸 공백 맞춰야한다.
# shift+tab 을 하면 앞에 공백 지워짐

weather = "비"

if weather =="비":
    print("우산을 챙겨주세요.")

study_time = int(input("오늘의 공부시간을 입력해주세요"))

# 만약에 오늘 공부할 시간이 3시간 이상이라면 파이썬 공부
if study_time >=3:
    print("오늘은 파이썬 공부를 할거야!")

# 만약에 오늘 공부할 시간이 3시간 미만이라면 오늘은 놀자
if study_time < 3:
    print("오늘은 시간이 별로 없으니까 놀자!")

# 만약에 오늘 공부할 시간이 5시간 이상이고 7시간 이하라면 
# if study_time >=5 and 7 >=study_time:
if 7 >= study_time >=5:
    print("오늘은 자바 공부를 할거야!")