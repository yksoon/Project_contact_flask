import sqlite3

# 데이터베이스 연결
con = sqlite3.connect('contact.db', check_same_thread=False)

# cursor 객체 만들기
cursor = con.cursor()

# 테이블 생성
# cursor.execute("CREATE TABLE contact(no INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, number TEXT)")
# cursor.execute("INSERT INTO contact(name, number) VALUES('abcdd', '01011113333')")

# print(cursor.execute("SELECT * FROM contact"))
# cursor.fetchone()
# con.commit()

# 리스트 출력
def select_list():
    cursor.execute("SELECT * FROM contact")
    sel_list = cursor.fetchall()
    return sel_list

# 연락처 추가
def insert_contact(name, phone):
    query = "INSERT INTO contact(name, number) VALUES('{}','{}')".format(name, phone)
    cursor.execute(query)
    con.commit()

# 연락처 삭제


