# 셀리니움_웹드라이버_네이버로그인.py
# pip install clipboard 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

#driver = webdriver.Chrome(ChromeDriverManager().install()) # 웹드라이버로 크롬 제어하려고..
driver = webdriver.Chrome() # 버전 올라가면 설치안됨 ChromeDriverManager().install()
driver.get('https://nid.naver.com/nidlogin.login')

# 네이버 메인화면에서 로그인 버튼 클릭
# driver.find_element_by_xpath('//*[@id="account"]/a').click()
# time.sleep(1)   # 1초 시간 지연

# 로그인 창에 아이디/비밀번호 입력
loginID = "sungpro3"
clipboard.copy(loginID)
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v') # 현재 문서의 모든 계층에서 []안의 속성이 id인거에 붙여넣기

loginPW = "1234"
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

#창이 닫히면 안되니깐 일부러 무한루프 넣어둔다..
while True:
    pass 