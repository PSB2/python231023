#전역변수
str = "Not Class Member"
class GString:
    def __init__(self):
        #멤버변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #self누락
        print(str) #-> self.str를 해야한다. 아니면 적역변수의 str을 참조한다...

g = GString()
g.set("First Message")
g.print()
