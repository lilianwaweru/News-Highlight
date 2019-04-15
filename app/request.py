from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the new base url
base_url = app.config["NEWS_API_BASE_URL"]


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

# def get_news(id):
#     get_news_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_news_details_url) as url:
#         news_details_data = url.read()
#         news_details_response = json.loads(news_details_data)

#         news_object = None
#         if movie_details_response:
#             id = news_details_response.get('id')
#             name = news_details_response.get('original_name')
#             description = news_details_response.get('description')
#             url = news_details_response.get('url')
#             category = news_details_response.get('category')
#             country = news_details_response.get('country')

#             news_object = news(id,title,overview,poster,vote_average,vote_count)





