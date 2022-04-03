# 문자열 포매팅
weather = "맑음"
temperature = 20
chance_shower = 33.5
print("오늘의 날씨는", weather,"기온은",temperature,"도 입니다.")

print("오늘의 날씨는 %s 기온은 %d도 입니다."%(weather,temperature))
print("오늘의 날씨는 {}이며, 기온은 {}도 입니다.".format(weather,temperature))

# %
print("오늘의 날씨는 %s 기온은 %d도 비가 내일 확률은 %d%%입니다."%(weather,temperature,chance_shower))
print("오늘의 날씨는 %s 기온은 %d도 비가 내일 확률은 %f%%입니다."%(weather,temperature,chance_shower))
print("오늘의 날씨는 %s 기온은 %d도 비가 내일 확률은 %.1f%%입니다."%(weather,temperature,chance_shower))

# format
print("오늘의 날씨는 {} 기온은 {}도 비가 내일 확률은 {}입니다.".format(weather,temperature,chance_shower))
print("오늘의 날씨는 {0} 기온은 {2}도 비가 내일 확률은 {1}입니다.".format(weather,temperature,chance_shower))

print("{},{}".format(weather,temperature))
print("{:10},{:10}".format(weather,temperature))
print("{0:},{1:d},{1:f},{1:o},{1:x}".format(weather,temperature))
# o 8진수 x 16진수

left ="left"
right = "right"
middle ="middle"

# !@#<>^
print("({2:>10s}),({1:^10s}), ({0:<10s})".format(left, middle, right))
print("({2:!>10s}),({1:@^10s}), ({0:#<10s})".format(left, middle, right))
print("({2:!>10.4s}),({1:@^10.3s}), ({0:#<10.2s})".format(left, middle, right))

#f-string

weather = "맑음"
temperature = 20

print(f"오늘의 날씨는 {weather}이며, 기온은 {temperature}도 입니다.")

print(f"2곱하기 30의 결과값 = {2*30}")
