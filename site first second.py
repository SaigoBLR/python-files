#from flask import Flask,render_template
#app = Flask(__name__)

#@app.route('/templates/')
#@app.route('/templates/<name>')
#def hello(name=None):
#    return render_template('template.html', name=name)


from flask import Flask,render_template
app = Flask(__name__)

@app.route('/first.html')
#@app.route('/first/<name>')
def first():
    return render_template('first.html')

@app.route('/second.html')
#@app.route('/second/<name>')
def second():
    return render_template('second.html')


