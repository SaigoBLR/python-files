class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author
conauth1 = Post('Название 1','Содержание 1','Автор 1')
conauth2 = Post('Название 2','Содержание 2','Автор 2')
conauth3 = Post('Название 3','Содержание 3','Автор 3')

all_news = [conauth1,conauth2,conauth3]

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/posts')
def list_news():
    return render_template('news_temple.html', novosti= all_news)

@app.route('/posts/<news_id>')
def view_news(news_id):
    news_id_int = int(news_id)
    news = all_news[news_id_int]
    return render_template('view_news.html',news = news)