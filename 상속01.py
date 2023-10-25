# 부모 클래스
class Person:  #-> Person(object)에서 object 생략 상속 생략
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    def working(self):
        print("현재 작업중")
    def sleeping(self):
        print("현재 수면중")        
# 자식 클래스
class Student(Person): #-> Person을 상속받는의미
    #-> 초기화 매서드 덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #self.name = name
        #self.phoneNumber = phoneNumber
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    # 상속받은 메서드 덮어쓰기..
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))  
    def printInfo(self):
        print("Info(학과:{0}, 학번: {1})".format(self.subject, self.studentID))          

# 인스턴스
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "20231024")
print(p.__dict__) # -> object class에 있는 __dict__호출.. 위에 양식이 dict양식
print(s.__dict__)
p.printInfo()
s.printInfo() #-> person에 있는 printInfo를 불러옴. 따라서 student에서 재정의 필요
p.sleeping()
p.working()


