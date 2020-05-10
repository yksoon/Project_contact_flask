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
    cursor.execute("SELECT * FROM contact ORDER BY name")
    sel_list = cursor.fetchall()
    return sel_list

# 연락처 추가
def insert_contact(name, phone):
    query = "INSERT INTO contact(name, number) VALUES('{}','{}')".format(name, phone)
    cursor.execute(query)
    con.commit()

# 연락처 상세보기
def select_detail(no):
    query = "SELECT * FROM contact WHERE no='{}'".format(no)
    cursor.execute(query)
    sel_detail = cursor.fetchall()
    return sel_detail

# 연락처 수정
def update_contact(no, name, phone):
    query = "UPDATE contact SET name='{}', number='{}' WHERE no={}".format(name, phone, no)
    cursor.execute(query)
    con.commit()
    
# 연락처 삭제
def delete_contact(no):
    query = "DELETE FROM contact WHERE no=%s" % no
    cursor.execute(query)
    con.commit()

# 연락처 검색
def search_contact(name):
    query = "SELECT * FROM contact WHERE name='{}'".format(name)
    cursor.execute(query)
    sel_search = cursor.fetchall()
    return sel_search

