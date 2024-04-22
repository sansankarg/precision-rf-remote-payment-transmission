import sqlite3
from flask import Flask, render_template, request
from call_database import connect as con

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Database/data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def main():
    return render_template('Main.html')

@app.route('/transaction.html')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM userdata').fetchall()
    conn.close()
    return render_template('transaction.html', posts=posts, host = "5;url=http://127.0.0.1:5000/transaction.html")

@app.route('/transaction.html', methods=['POST'])
def json():
    dat = request.get_json()
    print(dat['sender'])
    print(dat['reciever'])
    print(dat['ar'])
    con.update_transact_data(self=con, data = dat)
    return render_template('transaction.html', posts=dat)


@app.route('/creacc.html', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        load = {'id' : id, 'name' : name}
        if con.update_new_account(self=con, data=load):
            return render_template('creacc.html', msg = "New Account Created")
        else:
            return render_template('creacc.html', msg = "Account already exists")
    return render_template('creacc.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)