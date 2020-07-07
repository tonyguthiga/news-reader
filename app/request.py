from app import app
import urllib.request,json
from app.models import News, Articles
import requests 


#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
article_base_url = app.config["ARTICLE_API_BASE_URL"]

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
        news_sources: A list of news objects 
    '''
    news_sources = []
    for news_item in news_list:
        name = news_item.get('name')
        url = news_item.get('url')

        if name:
            new_object = News(name,url)
            news_sources.append(new_object)

    return news_sources

def get_articles():
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = article_base_url.format(api_key)

    get_articles_response = requests.get(get_article_url).json()

    news_articles = None 

    if get_articles_response['articles']:
        news_articles_list = get_articles_response['articles']
        news_articles = process_articles(news_articles_list)
    
    return news_articles

def process_articles(articles_list):
    '''
    Function that processes the news articles and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain news details

    Returns:
        news_articles: A list of news objects 
    '''
    news_articles = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        if urlToImage:
            article_object = Articles(author, title, description, url, urlToImage, publishedAt)
            news_articles.append(article_object)

    return news_articles