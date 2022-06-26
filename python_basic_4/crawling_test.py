# 웹 크롤링 = 웹 스크립핑
# 필요한 정보만 추출하는 것
# requests 요청 
# BeautifulSoup

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.naver.com")
bs = BeautifulSoup(r.content,"html.parser")

# h3 = bs.select("h3")
# h3 = bs.select_one("h3")
# h3 = bs.select_one("h3 > a")
# h3 = bs.select_one("div.current_box")
# selecter = bs.select_one("div.current_box")
# selecter = bs.select(".title")
# selecter = bs.find_all("div", {"class":"partner_box"})
selecter = bs.find("div", {"class":"partner_box"})

print(selecter.text)

# print(h3.text)
# print(h3[0].text)
# print(h3[0].name)
# print(h3[0].attrs)
# print(h3)
print(selecter)


