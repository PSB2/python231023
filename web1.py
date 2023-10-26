# web1.py
# 웹크롤링
from bs4 import BeautifulSoup #BeautifulSoup 만 메모리에 탑재...

#페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체 생성. soup에다 페이지 내용을 다 올려놓는다.
soup = BeautifulSoup(page, "html.parser") #클래스생성 후 초기화
#html, xml(저장,교환할때 사용) html을 파싱하려고 적용

#전체보기
#print(soup.prettify())
#<p>태그 전체를 검색
#print(soup.find_all("p")) #리스트 형태로 찾아서 반환. 변형된 리스트임.
# 첫번째 <p>만 검색
#print(soup.find("p")) 
#<p class="outer-text"> 형태만 검색
#print(soup.find_all("p", class_="outer-text")) # class는 python의 키워드라 _ 빼면 에러남..
# attrs를 사용(Attributes) 이걸 제일 많이 사용
#print(soup.find_all("p", attrs={"class":"outer-text"}))
#특정 태그만 지정할 경우 id 속성.
print(soup.find_all(id="first")) #id는 일종의 태그 이름..id가 first인 것만 가져옴..
#태그 내부의 컨텐츠를 가져오기: .text
for tag in soup.find_all("p"):
    title = tag.text.strip() #택스트만 가져옴..
    title = title.replace("\n","") #빈줄 없애기..
    print(title)

