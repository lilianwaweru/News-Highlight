from app import app
import urllib.request,json
from .models import Articles, News

News = news.News
Articles = articles.Articles

#Getting api key
api_key = None


#Getting the new base url
base_url = None
base_url_articles = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    base_url_articles = app.config[' ARTICLES_API_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def get_articles(id):
    '''
    function that gets the json response to our url request
    '''
    get_articles_url = base_url_articles.format(id,api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results = process_articles(get_articles_response['articles'])


    return articles_results


def process_results(news_list):
    '''
    Function that processes the news results and transforms them to a list of objects
    Args:
        news_list:A list of dictionaries that contain news details
    Returns:
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        
        news_object = News(id,name,description,url,category,country)
        news_results.append(news_object)

    return news_results  


def process_articles(articles_list):
    '''
    Function that processes the articles results and transforms them to a list of objects
    Args:
        articles_list:A list of dictionaries that contain articles details
    Returns:
        articles_results: A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        description =articles_item.get('description')
        publishedAt = articles_item.get('publishedAt')
        
        articles_object = Articles(author,title,url,urlToImage,description,publishedAt)
        articles_results.append(articles_object)

    return articles_results  

