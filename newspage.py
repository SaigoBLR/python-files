class News:
    def __init__(self,title,content):
        self.title = title
        self.content = content

news1 = News('Заголовок 1','Новость 1')
news2 = News('Заголовок 2','Новость 2')
news3 = News('Заголовок 3','Новость 3')

news = [news1,news2,news3]

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/newstemple/')
#@app.route('/newstemple/<news>')
def News(news = None):
    return render_template('newstemple', news= news)




