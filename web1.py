# web1.py
# 웹크롤링
from bs4 import BeautifulSoup #BeautifulSoup 만 메모리에 탑재...

#페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체 생성.
soup = BeautifulSoup(page, "html.parser") #클래스생성 후 초기화
#html, xml(저장,교환할때 사용) html을 파싱하려고 적용

#전체보기
print(soup.prettify())