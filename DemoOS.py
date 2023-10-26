# DemoOS.py
from os.path import*
from os import *
import glob

print("전체경로", abspath("python.exe")) # os.path.abspath 붙여야하나 생략.
print("파일명", basename("c:\\work\\demo.txt")) # demo.txt만 보여줌 경로빼고.

#strPython = "c:\\python310\\python.exe" # \\두번쓰는 이유는 \n 이렇게 오해할 수 있어서 두번씀.
strPython = r"c:\python310\python.exe" # 약식으로 특수문자로 가공하지 않은 상태(raw string notation)
if exists(strPython):
    print("파일크기:{0}".format(getsize(strPython)))
else:
    print("파일없음")

# 외부 실행파일
#system("notepad.exe") #노트패드 실행..

# 운영체제..
print("운영체제 이름:", name)
print("환경변수:", environ)

#result = glob.glob("c:\\work\\*.py")
#print(result)

for item in glob.glob("c:\\work\\*.*"):
    print(item)
