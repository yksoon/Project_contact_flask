from flask import Flask, render_template, redirect, request
from dao import select_list, insert_contact

app = Flask(__name__)



@app.route('/')
def main():
    global sel_list
    sel_list = select_list()
    return render_template('mainlist.html', select_list=sel_list)

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

@app.route('/detail/<no>')
def detail(no):
    

if __name__ == '__main__':
    app.run(debug = True)