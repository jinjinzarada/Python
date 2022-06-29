import requests
from bs4 import BeautifulSoup

r = requests.get("https://vibe.naver.com/today")
bs = BeautifulSoup(r.text, "html.parser")

#가수의 목록
# 노래의 목록

song_name = []
artist_name = []

song = bs.select("td.name > a > span.ellipsis")
artist = bs.select("td_artist > a > span.ellipsis")

print(artist)
print(song)

for s in range(len(song)):
    song_name.append(song[s].text)
for a in range(len(song)):
    artist_name.append(artist[a].text)
for i in range(0,50):
    print(f"순으; {i+1}위 - 가수 : {artist_name[i].strip()} - 곡명 : {song_name[i]}")

