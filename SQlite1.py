import sqlite3

# DB 연결 (DB가 없는 경우, 새로운 DB 파일 생성, 아나콘다 설치하면 같이 설치됨)
conn = sqlite3.connect('/Users/YB/Downloads/5674-849/output/sample2.db')
print(conn)

# Connection 객체에서 Cursor 생성
cur = conn.cursor()
print(cur)

sql = '''
CREATE TABLE Product(
id integer primary key autoincrement,
title text not null,
price integer,
link text)
'''

cur.execute(sql)

# DB 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()