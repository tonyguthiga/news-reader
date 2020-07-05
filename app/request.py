from app import app
import urllib.request,json
from .models import news
import requests 

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    get_news_response = requests.get(get_news_url).json()

    news_sources = None 

    if get_news_response['sources']:
        news_sources_list = get_news_response['sources']
        news_sources = process_sources(news_sources_list)
    
    return news_sources

def process_sources(news_list):
    '''
    Function that processes the news sources and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns:
        news_articles: A list of news objects 
    '''
    news_sources = []
    for news_item in news_list:
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

    if name:
        new_object = News(name,description,url,category)
        news_sources.append(new_object)

    return news_sources

