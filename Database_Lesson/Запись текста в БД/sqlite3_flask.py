from flask import Flask,request
import sqlite3
app = Flask(__name__)
app.cathall = False

@app.route('/', methods=['POST'])
def data():
    if request.method == 'POST':
        data = request.data.decode("utf-8")
        con = sqlite3.connect('C:\\db\\test.db')

        cur = con.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS test_table(Comment TEXT)')

        params = (data,)

        cur.execute('INSERT INTO test_table VALUES(?)',params,)
        con.commit()

        cur.close()
        con.close()

if __name__== "__main__":
    app.run(host="127.0.0.1", port=5000)