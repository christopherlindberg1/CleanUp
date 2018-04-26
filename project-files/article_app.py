from bottle import route, run, template
import article_collection

@route('/')
def index():
    articles = article_collection.get_articles()
    return template('index', articles=articles)

run(host='localhost', port=8080)
