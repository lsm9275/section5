import sqlite3
import simplejson as json
import datetime

#DB생성(파일)
conn = sqlite3.connect('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section5/database/sqlite1.db')

#날짜 생성
now = datetime.datetime.now()
print('now',now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime',nowDatetime)

#sqlite3 버전확인
print('sqlite3.version : ',sqlite3.version)
print('sqlite3.sqlite_version',sqlite3.sqlite_version)

#DB생성 & Autocommit
conn = sqlite3.connect('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section5/database/sqlite1.db', isolation_level=None)

#DB생성(메모리)
#conn = sqlite3.connect(":memory:")

#Cursor연결
c = conn.cursor()
print(type(c))

#테이블 생성(SQLite3 Datatype : TEXT NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)") #AUTOINCREMENT

#데이터 삽입
#c.execute("INSERT INTO users VALUES (1 ,'kim','kim@naver.com', '010-0000-0000', 'kim.com', ?)", (nowDatetime,))
#c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", (2, 'park', 'park@naver.com', '010-1111-1111', 'park.com', nowDatetime))

#Many 삽입(튜플, 리스트 가능)
userList = (
    (3 ,'lee','lee@naver.com', '010-2222-2222', 'lee.com', nowDatetime),
    (4 ,'cho','cho@naver.com', '010-3333-3333', 'cho.com', nowDatetime),
    (5 ,'noh','noh@naver.com', '010-4444-4444', 'noh.com', nowDatetime)
)
#데이터 삽입
#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",userList)

#json삽입
with open('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section5/data/users.json', 'r') as infile:
    r = json.load(infile)
    userData = []
    for user in r:
        t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
        #print('t', t)
        userData.append(t)
    #print('userData', userData)
    #print('userData', tuple(userData))
    c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",userData)


c.execute("CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, userId INTEGER, title text, completed text, regdate text)")

with open('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section5/data/todos.json', 'r') as infile:
    r = json.load(infile)
    todoData = []
    for todo in r:
        t = (todo['id'], todo['userId'], todo['title'], todo['completed'], nowDatetime)
        #print('t', t)
        todoData.append(t)
    c.executemany("INSERT INTO todos(id, userId, title, completed, regdate) VALUES (?,?,?,?,?)", todoData)
#print("users db delete", conn.execute("delete from users").rowcount,"rows")
conn.commit()

conn.close()










'''
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

#JSON to Sqlite 삽입1
with open('C:/Django/workspace/python-class1/section5/data/users.json','r') as infile:
    r = json.load(infile)
    userData = []
    for user in r:
        t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
        userData.append(t)
    #c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userData)
    c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", tuple(userData))

#JSON to Sqlite 삽입2
with open('C:/Django/workspace/python-class1/section5/data/users.json','r') as infile:
    r = json.load(infile)
    for user in r:
        c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime))

#테이블 Row 삭제
print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

#커밋
conn.commit()

#롤백
#conn.rollback()

#접속 해제
conn.close()
'''