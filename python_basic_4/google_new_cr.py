# 웹페이지 들어가지 않고 뉴스검색, 기사제목, 본문, 링크, 게시글날짜를 엑셀에 담아 출력
# 뉴스 검색, 기사제목, 링크를 리스트에 담아서 출력

import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://news.google.com/search?q=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text, "html.parser")

# 기사제목, 링크

titles = bs.select("div.xrnccd > article > h3 > a")

news = []

for i in titles:
    title = i.text
    links = "https://news.google.com" + i.get("href")[1:]

    news.append([title,links])
    google_news_df = pd.DataFrame(news, columns=["기사제목","링크주소"])

google_news_df.to_excel("뉴스크롤링 결과.xlsx")

print("저장성공!!")