from flask import Flask, render_template, redirect, request
from dao import select_list, insert_contact, select_detail, update_contact, delete_contact, search_contact

app = Flask(__name__)


# 기본 접속
@app.route('/')
def main():
    global sel_list
    sel_list = select_list()
    return render_template('mainlist.html', select_list=sel_list)

# 연락처 추가
@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        name = str(request.form['name'])
        phone = str(request.form['phone'])
        insert_contact(name, phone)
    return redirect('/')

# 연락처 상세보기
@app.route('/detail/<no>')
def detail(no):
    global sel_detail
    sel_detail = select_detail(no)
    return render_template('detail.html', select_detail=sel_detail)

# 연락처 수정
@app.route('/updatepage/<no>')
def updatepage(no):
    global sel_detail
    sel_detail = select_detail(no)
    return render_template('update.html', select_detail=sel_detail)

@app.route('/update/<no>', methods=['GET', 'POST'])
def update(no):
    if request.method == 'POST':
        name = str(request.form['name'])
        phone = str(request.form['phone'])
        update_contact(no, name, phone)
        return redirect('/detail/%s' % no)

# 연락처 삭제
@app.route('/delete/<no>')
def delete(no):
    delete_contact(no)
    return redirect('/')

# 연락처 검색
@app.route('/search', methods=['GET', 'POST'])
def search_page():
    if request.method == 'POST':
        name = str(request.form['name'])
        return redirect('/search/%s' % name)

@app.route('/search/<name>')
def search(name):
    global sel_list
    search = search_contact(name)
    return render_template('search.html', search=search)    

if __name__ == '__main__':
    app.run(debug = True)