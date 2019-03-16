from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def Main() :
    return render_template('main.html')

@app.route('/video')
def Video() :
    return render_template('video.html')

@app.route('/text')
def Text() :
    return render_template('text.html')