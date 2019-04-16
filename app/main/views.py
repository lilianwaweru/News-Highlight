from flask import render_template
from .main import main
from ..request import get_news,get_articles


@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    #Getting sports news
    sports_news = get_news('sports')
    # print(sports_news)
    business = get_news('business')
    entertainment = get_news('entertainment')
    technology = get_news('technology')
    title = 'Home - Welcome to the Best News Review Website Online'
    return render_template('index.html',title = title, sports = sports_news, business = business, entertainment = entertainment, technology = technology)

@main.route('/articles/<id>')
def news_articles(id):
    '''
    A function that will return news articles plus data
    '''
    news_articles = get_articles(id)
    return render_template('articles.html', id = id, articles = news_articles )












