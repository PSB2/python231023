# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
#이게 비어있으면 웹로봇이라 가정해서 막아버린다. 크롬. 엣지 접속은 헤더가 있으므로 헤더표시..
#구글링하면 크롬, 엣지 검색가능. User-agent
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일에 저장
f = open("c:\\work\\today.txt","wt", encoding="utf-8")
for n in range(1,11):
        #오늘의 유머 베스트 게시판
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우
        page = data.decode('utf-8', 'ignore') #문자열 깨져도 무시하겠다. utf-8로 인코딩.
        soup = BeautifulSoup(page, 'html.parser') 
        list = soup.find_all('td', attrs={'class':'subject'}) #태그는 주소별로 틀리니 바꿔줘야함. span -> td data-role->class

# <td class="subject">
# <a href="/board/view.php?table=bestofbest&amp;no=471497&amp;s_no=471497&amp;page=1" target="_top">우리나라 지금 현재 전쟁나면 필패인 이유 추가</a><span class="list_memo_count_span"> [18]
# </span>  </td>

        for item in list:
                #에러처리(try ~ catch)
                try:
                        title = item.find("a").text.strip()
                        #title = item.text.strip()
                        if re.search("미국", title): # 미국이 포함된 title만 나온다...
                            print(title)
                            f.write(f"{title}\n")
                        #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling # nextSibling 이웃사촌, 바로 옆에...
                        # title = span2.text 
                        # if (re.search('아이폰', title)):
                        #         print(title.strip())
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
f.close()