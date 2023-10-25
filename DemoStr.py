# DemoStr.py

strA = "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p", 7)) # 7 번부터 셀것..
print(strB.startswith("python"))
print(strB.endswith("ful"))
print("MBC2580".isalnum()) #알파벳숫자인지..
print("MBC:2580".isalnum())
print("2580".isdecimal())#숫자만인지ㅣ....
#앞뒤에 공백문자 제거(데이터 전처리)
data = "<<< spam and ham >>>"
result = data.strip("<> ") # 3개를 넣는다. < > 빈칸 없애라...
print(data)
print(result)
result2 = result.replace("spm", "spam egg")
print(result2)
#화이트스페이스(지정안하면 공백 기준으로 자른다..)
result2 = "spam::egg::ham"
lst = result2.split("::") # ::잘라라...
print("리스트: ", lst)
print("------다시 합치기------")
print(":)".join(lst))