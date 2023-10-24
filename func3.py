#필터링하는 함수
lst = [10, 25, 30]
iterL = filter(None, lst) #None은 널의미 필터링 조건이 없다...
for item in iterL: 
    print(item)

print("------ 필터링하는 경우")
def getBiggerThan20(i): #i가 20보다 큰것만...
    return i > 20

iterL = filter(getBiggerThan20, lst) #파이썬은 참조가 전달됨...함수 참조가 전달....
for item in iterL:
    print(item)

#람다함수 적용 
print("------ 람다함수-------") #람다를 쓰면 간결해짐..
iterL = filter(lambda x:x>20 , lst) #람다를 필터조건으로..x를 입력받아 x가 20보다 큰것만 가져온다..
for item in iterL:
    print(item)

#분기구문
#선택한 블럭 주석: ctrl + /
# score = int(input("점수를 입력: "))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"    
# else:
#     grade = "D"

# print("등급은 ", grade)    

#반복문
value = 5
while value > 0:
    print(value)
    value -= 1


lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))

fruit = {"apple":100, "kiwi":200}
for item in fruit.items():
    print(item)

#수열함수
lst = list(range(1,11))
print(lst)
print("------break구문--------")
for i in lst:
    if i > 5 :
        break
    print("Item:{0}".format(i))

print("------continue구문------")
for i in lst:
    if i % 2 == 0 :
        continue
    print("Item:{0}".format(i))

print("----------수열함수----------")
print(list(range(2000,2024))) # 2024앞까지...생성함..
print(list(range(1,32)))# 1~31까지생성..

for i in range(5): #수동으로 5번돔..
    print(i)
