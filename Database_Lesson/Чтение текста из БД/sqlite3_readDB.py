from flask import Flask,request
import sqlite3
app = Flask(__name__)

@app.route('/')
def readDB():
    con = sqlite3.connect('C:\\db\\test.db')
    cur = con.cursor()
    cur.execute('SELECT comment FROM test_table')
    data = cur.fetchall()
    cur.close()
    con.close()
    return data[0][0]

if __name__== "__main__":
    app.run(host="127.0.0.1", port=5000)