#from flask import Flask,render_template
#app = Flask(__name__)

#@app.route('/templates/')
#@app.route('/templates/<name>')
#def hello(name=None):
#    return render_template('template.html', name=name)
class News:
    def __init__(self,title,news):
        self.title = title
        self.news = news

p_news1 = News('Заголовок 1','Новость 1')
p_news2 = News('Заголовок 2','Новость 2')
p_news3 = News('Заголовок 3','Новость 3')

lst = [p_news1,p_news2,p_news3]

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/first.html')
@app.route('/first.html/<news>')
def first(news = None):
    return render_template('first.html', news= lst)




