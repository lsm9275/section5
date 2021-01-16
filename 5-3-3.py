import sqlite3

#DB생성(파일)
conn = sqlite3.connect('D:/6_PWork/5_inflearn/01_Python_Automation_and_GUI/Section5/database/sqlite1.db')

#cursor indication
c = conn.cursor()

c.execute("UPDATE users SET username=? WHERE id=?", ('niceman',1))
c.execute("UPDATE users SET username= :name WHERE id=:id", {'name': 'goodboy', 'id':2})
c.execute("UPDATE users SET username='%s' WHERE id='%s'" %('cuteboy',3))
conn.commit()
