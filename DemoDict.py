# DemoDict.py

phone = {"kim" : "111", "lee":"3333", "park":"3333"}
print(phone)
print(len(phone))
print(phone["kim"])
#include의 약자(멤버쉽)
print("park" in phone)
print("kang" not in phone)

p = phone

p["kang"] = "1234"

print(p)
print(phone)
print( id(phone), id(p) ) 

#장비 관리
device = {"아이폰":5, "아이패드":10}
print(device["아이폰"])
#입력
device["맥북"] = 15
device["패드프로"] = 100
device["아이맥"] = 400000
#수정
device["아이폰"] = 6
print(device)
#삭제
del device["아이폰"]
print(device)

for item in device.items():
    print(item)

for item in device.keys():
    print(item)

for item in device.values():
    print(item)        


print(bool(0))    
print(bool(3))  
print(bool(""))  
print(bool("test"))
print(bool([])) 
print(bool([1,2,3])) 
print("---논리식-----")
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and True)
print(True and True and False)
print(True or False or False)
print(5/2)
print(5//2)
print(5%2)