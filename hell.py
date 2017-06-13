from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about project page'

@app.route('/templates/')
@app.route('/templates/<name>')
def hello(name=None):
    return render_template('template.html', name=name)
