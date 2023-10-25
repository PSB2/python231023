#정규표현식
import re 

#원본 로그파일
f=open('c:\\work\\PV3.txt','rt')
#복사본 파일
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''): # eof가 아니면 ''는 eof의미 비어있지 않으면...
    if (re.search("error", line)): #숫자가 연속으로 4자리 있으면 찾으면.. \d{4}, error
        g.write(line + "\n") # 줄바꾸고 다음줄로 이동..
    line = f.readline() # 연도 패턴만 따로 가져옴..

f.close() 
g.close()








