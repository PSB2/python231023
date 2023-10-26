# db1.py
import sqlite3

#연결객체(일단은 메모리에 저장)
con = sqlite3.connect(":memory:")
#커서객체../
cur = con.cursor()
#테이블 구조 생성....
cur.execute("""create table if not exists PhoneBook
(id integer primary key autoincrement, name text, phoneNum text);
""") #앞에 쌍따옴표 있으면 줄바꿈해도 상관없다..

#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('전우치','101-222');")

#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-333"
cur.execute("insert into PhoneBook (name, phoneNum) values (?,?);",(name, phoneNumber)) 
#?는 치환한다는 뜻. name, phonenumber를 묶어서 튜플로 묶어서 던져줌..

#다중으로 행을 입력
datalist =(("박문수","010-333"),("김길동","010-567"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?,?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)
print("-------fetchone()--------")
print(cur.fetchone()) # db에 있는걸 임시 버퍼에 두고 보여주고 사라짐. 안사라지는것도 있음
print("-------fetchmany(2)--------")
print(cur.fetchmany(2)) # 책갈피(Record Pointer)가 다음 버퍼에있어서 보여주고 사라짐. 
print("-------fetchall()--------")
#cur.execute("select * from PhoneBook;") # 다시 채워두면 4개 다보여줌..
print(cur.fetchall()) # 버퍼에 한개 밖에 안남았으니 1개만 보여줌..