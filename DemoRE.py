# DemoRE.py
# 정규표현식(특정한 규칙)
import re

result = re.search("[0-9]*th", "  35th") #[0-9]* 0~9숫자가 여러번 나와도 됨. * 여러번의미
print(result)
print(result.group()) # 찾은 문자열만 보여주게..group()
#함정 추가*(ctrl + /)
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group()) # 매치함수가 리턴하는게 없어서 에러남. NoneType

result = re.search("apple", "this is Apple".lower()) #대소문자 구별함..Apple은 에러..
print(result.group())

result = re.search("\d{4}", "올해는 2023년 입니다.") # 숫자뒤에 4자리 오는거 찾아라..
print(result.group())

result = re.search("\d{5}", "우리 동네는 52300") # d가 digit 숫자 5개...
print(result.group())

#컴파일 함수를 사용
data = "Apple is big company and apple is delicious"
c = re.compile("apple", re.IGNORECASE) # 문자가 엄청 길면 미리 해석필요..속도빠름. 대소문자 구분마라 옵션
print(c.findall(data)) # c는 컴파일된 객체..

data = """다중 라인으로
만든 문자열 

데이터"""
c = re.compile("^.+", re.MULTILINE) # 빈줄 제외 나머지 다 가져오게..
              # ^은 시작하는 패턴 시작 의미 $끝나는패턴.. .은 글자하나 의미 + 는 1~N번
              # 즉 시작할 때 글자가 한개라도 있어야한다는 의미..
print(c.findall(data))
