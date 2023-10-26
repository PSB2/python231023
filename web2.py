# web2.py
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response =requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#<div class속성 딕셔너리>
#파일에 저장
f = open("c:\\work\\dangn.txt","wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"}) #div 태그 안의 class가 card-desc인거 찾아라..
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"}) #h2태그의 클래스가 카드 클래스인거 가져오기..
    price = post.find("div", attrs={"class":"card-price"})
    addr = post.find("div", attrs={"class":"card-region-name"})
    title = title.text.strip().replace("\n","")
    price = price.text.strip().replace("\n","")
    addr = addr.text.strip().replace("\n","")
    print("{0}, {1}, {2}".format(title, price, addr))
    #f를 붙이고 변수명 넘기기
    f.write(f"{title},{price}, {addr}\n") # f는 포맷, 파일의 약자.. 이렇게 약어로 많이씀
    
f.close()

# <div class="card-desc">
#       <h2 class="card-title">다이슨청소기</h2>
#       <div class="card-price ">
#         50,000원
#       </div>
#       <div class="card-region-name">
#         대구 수성구 범어2동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 28
#           </span>
#         ∙
#         <span>
#             채팅 26
#           </span>
#       </div>
#     </div>