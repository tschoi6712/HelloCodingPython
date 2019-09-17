""""""""""""""""""""""
외부모듈

pip install '모듈이름'
conda install '모듈이름'
"""""""""""""""""""""""


# BeautifulSoup 모듈로 웹페이지 분석하기 - 날씨 가져오기
from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):                # location 태그를 찾기
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)




