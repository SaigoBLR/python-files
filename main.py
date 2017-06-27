
from flask import Flask,render_template
app = Flask(__name__)


class News:
    def __init__(self,title,content):
        self.title = title
        self.content = content


# some example news
news1 = News('Заголовок 1','Новость 1')
news2 = News('Заголовок 2','Новость 2')
news3 = News('Заголовок 3','Новость 3')

all_news = [news1,news2,news3]


# we want default page (e.g. http://mysite.com/) to show the list of all news
@app.route('/')
def list_news():
    # the arguments to `render_template` are:
    #   * 'list_news.html' - name of a template file respective to "templates" subdirectory,
    #                        e.g. `<ROOT>/templates/list_news.html`
    #   * `all_news` - the object (news list) we want to pass to the template
    #   * `all_available_news` - the name that we will use on the template for this object
    return render_template('list_news.html', all_available_news=all_news)



# we also want to view individual news by their number in `all_news`
# to do so, we will use path parameters - a thing in the `< >` brackets
# when we enter `http://mysite.com/news/42`, Flask will capture number 42 for us
# and call `view_news` with it as parameter `news_id`
@app.route('/news/<news_id>')
def view_news(news_id):
    news_id_int = int(news_id)     # Flask parses <news_id> to a string by default,
                                   # we need to convert it to a number first
    news = all_news[news_id_int]   # take specific news from `all_news` by its ID (number in the list)
    # `news=news` means that we pass a python object `news` to the template and give it there
    # exactly the same name - `news`
    return render_template('view_news.html', news=news)



# another version which does exactlt the same thing, but have several differences in implementation:
#   * path is a bit different (`news2` instead of `news`)
#   * path parameter has converter (`int:`); this way Flask will convert `news_id`
#     from string to int automatically
#   * object name here in python (`current_news`) is different from the object name on the template (`news`),
#     but it doesn't play a role, since we pass it to the temlate under the name `news` as it expects it
# now you can open http://localhost:5000/news/1 or http://localhost:5000/news2/1 and see exactly the same thing
@app.route('/news2/<int:news_id>')
def view_news2(news_id):
    current_news = all_news[news_id]
    return render_template('view_news.html', news=current_news)
