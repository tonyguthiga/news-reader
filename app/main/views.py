from flask import render_template,request,redirect
from . import main
from ..requests import get_news, get_articles

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    news_sources = get_news()
    news_articles = get_articles()
    title = 'Home - Welcome to News-reader website for the best preview of news articles'
    return render_template('index.html', title = title, news_sources = news_sources, news_articles = news_articles)

@main.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that returns the news details page and its data
    '''
    #Getting news articles
    title = 'Home - News ID '
    return render_template('news.html',title = title)